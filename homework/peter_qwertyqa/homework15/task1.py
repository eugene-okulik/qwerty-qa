import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# --------------- task 1 ---------------------
task1_query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(task1_query, ('Gleb', 'Taskov 3'))
student_id = cursor.lastrowid
# print(student_id)

# --------------- task 2 ---------------------
task2_query = '''
INSERT INTO books (title, taken_by_student_id) VALUES
(%s, %s);
'''
task2_values = [('Book Python', student_id),
                ('Book Java', student_id)]
cursor.executemany(task2_query, task2_values)

# --------------- task 3 ---------------------
task3_query = '''
INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)
'''
cursor.execute(task3_query, ('Math group', 'sep 25', 'sep 26'))
group_id = cursor.lastrowid
# print(group_id)

task3_query_update = '''
UPDATE students SET group_id = %s
WHERE id = %s
'''
cursor.execute(task3_query_update, (group_id, student_id))

# --------------- task 4 ---------------------
task4_query = '''
INSERT INTO subjects (title) VALUES (%s)
'''
task4_values = [
    ('QA Subject 111',),
    ('QA Subject 222',),
    ('QA Subject 333',)
]
cursor.executemany(task4_query, task4_values)
# lastrowid return id of the first entered row
subject_ids = [cursor.lastrowid, cursor.lastrowid + 1]
# print(subject_ids)

# --------------- task 5 ---------------------
task5_query = '''
INSERT INTO lessons (title, subject_id) VALUES (%s, %s)
'''
task5_values = [
    ('QA Lesson 111', subject_ids[0]),
    ('QA Subject 222', subject_ids[0]),
    ('QA Subject 333', subject_ids[1]),
    ('QA Subject 444', subject_ids[1])
]
cursor.executemany(task5_query, task5_values)
lessons_id = [cursor.lastrowid + i for i in range(len(task5_values))]

# --------------- task 6 ---------------------
task6_query = '''
INSERT INTO marks (value, lesson_id, student_id) VALUES
(%s, %s, %s)
'''
task6_values = [
    (i, lessons_id[i], student_id) for i in range(len(task5_values))
]
cursor.executemany(task6_query, task6_values)
db.commit()


# --------------- Вывести все оценки студента ---------------------
query1 = '''
SELECT value AS 'marks' FROM marks WHERE student_id = %s
'''
cursor.execute(query1, (student_id,))
print(cursor.fetchall())


# --------------- Все книги, которые находятся у студента ---------------------
query2 = '''
SELECT title FROM books WHERE taken_by_student_id = %s
'''
cursor.execute(query2, (student_id,))
print(cursor.fetchall())

# -- Для вашего студента выведите всё, что о нем есть в базе --
query3 = '''
SELECT s.name, s.second_name,
g.title as 'group_name',
b.title as 'book_title',
m.value as 'mark_value',
l.title as 'lesson_title',
s2.title as 'subject_name'
FROM students s
JOIN `groups` g ON s.group_id = g.id
JOIN books b ON s.id = b.taken_by_student_id
JOIN marks m ON m.student_id = s.id
JOIN lessons l ON l.id = m.lesson_id
JOIN subjects s2 ON s2.id = l.subject_id
WHERE s.id = %s
'''
cursor.execute(query3, (student_id,))
print(cursor.fetchall())

db.close()

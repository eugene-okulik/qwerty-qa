import mysql.connector as mysql
import os
import dotenv
import csv


dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    database=os.getenv("DB_NAME")
)

query = '''
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
WHERE s.name = %s AND
s.second_name = %s AND
g.title = %s AND
b.title = %s AND
s2.title = %s AND
l.title = %s AND
m.value = %s
'''

cursor = db.cursor(dictionary=True)

base_path = os.path.dirname(__file__)
parent = os.path.dirname(os.path.dirname(base_path))
file_csv = os.path.join(parent, 'eugene_okulik',
                                'Lesson_16',
                                'hw_data',
                                'data.csv')

with open(file_csv) as file_cs:
    file_data = csv.DictReader(file_cs)

    for row in file_data:
        value = (row['name'],
                 row['second_name'],
                 row['group_title'],
                 row['book_title'],
                 row['subject_title'],
                 row['lesson_title'],
                 row['mark_value'])

        cursor.execute(query, value)

        if len(cursor.fetchall()) == 0:
            print(row)

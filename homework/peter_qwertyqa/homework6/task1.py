words = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
         "Integer urna nisl, facilisis vitae semper at, "
         "dignissim vitae libero")

words_list = words.split()
res = []

for word in words_list:
    if word.isalpha():
        word_new = word + "ing"
    else:
        word_new = word[:-1] + "ing" + word[-2:]
    res.append(word_new)

print(" ".join(res))

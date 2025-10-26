import argparse
import os
import re
from collections import defaultdict
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)


def file_split_to_timestamps(file_s):
    pattern = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})')
    res = defaultdict(list)
    cur_ts = None
    with open(file_s, "r") as f:
        for line in f:
            # Вернет объект match. Из него можно получить match.group,
            # .start, .end, .span - (start,end)
            timestamp_match = pattern.match(line)
            if timestamp_match:
                # получим сам таймстамп в формате datetime
                cur_ts = datetime.strptime(timestamp_match.group(),
                                           "%Y-%m-%d %H:%M:%S.%f")
                # вставляем до конца строки, тк знаем,
                # что новый таймстамп только с новой строки может быть
                res[cur_ts].append(line[timestamp_match.end()+1:])
            else:
                # если найти таймстамп не удалось,
                # добавляем строку в конец последнего таймстампа
                res[cur_ts].append(line)

    result = {}
    for k, v in res.items():
        result[k] = ''.join(v)
    return result


def find_word_neighbors(text, words):
    k = 0
    for word in words:
        k += 1
        if text in word:
            pos_min = max(k - 5, 0)
            pos_max = min(k + 5, len(words))
            res = ""
            for i in range(pos_min, pos_max):
                res += (words[i] + ' ')

            return res[:-1]

    return None


parser = argparse.ArgumentParser()

# Set arguments for the script: path and text
parser.add_argument("path", help="Path to sile or directory")
parser.add_argument("-t", "--text", help="Text to find in files")
args = parser.parse_args()
path, text_to_find = args.path, args.text

files = []

# If search text argument was not set, raise the ValueError
if text_to_find is None:
    raise ValueError("Search text cannot be empty. "
                     "Please use --text to enter the search text")

# /Users/bkh/test/qwerty-qa/homework/eugene_okulik/data/logs
# Check if the path exists and if its file or a directory
if os.path.isfile(path):
    files.append(path)
elif os.path.isdir(path):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            files.append(full_path)
else:
    # print("Path not found.")
    raise ValueError("Path not found.")


# Check if the directory is not empty
if len(files) == 0:
    print("Directory is empty. Nothing to find.")
else:
    # find all entries in files matching the text_to_find
    for file in files:
        res_dict = file_split_to_timestamps(file)

        # поиск слова в словаре
        for k, v in res_dict.items():
            if text_to_find in v:
                print(Fore.GREEN + "Found in file: "
                      + Style.RESET_ALL + os.path.basename(file))
                print(Fore.BLUE + "Timestamp (line): "
                      + Style.RESET_ALL + str(k) + "\n")
                print(find_word_neighbors(text_to_find, v.split()))
                print("\n")

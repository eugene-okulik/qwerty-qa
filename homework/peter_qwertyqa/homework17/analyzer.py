import argparse
import os

parser = argparse.ArgumentParser()

# Set arguments for the script: path and text
parser.add_argument("path", help="Path to sile or directory")
parser.add_argument("-t", "--text", help="Text to find in files")
args = parser.parse_args()
path, text_to_find = args.path, args.text

files = []

# If search text argument was not set, raise the ValueError
if text_to_find is None:
    raise ValueError("Search text cannot be empty. Please use --text to enter the search text")

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
    # TO-DO: find all entries in files matching the text_to_find
    print(files)



import re

import pyinputplus as pyip

PLACEHOLDERS = ('ADJECTIVE', 'NOUN', 'VERB')


def mad_libs(file_for_read, file_for_write):
    """Read content from file, replace words of speech with entered ones and save outcomes to new file."""
    with open(file_for_read, "r") as rf, open(file_for_write, "w") as wf:
        new_words = []
        for line in rf:
            for word in re.findall(r"[\w']+|[.]|\s", line):
                if word in PLACEHOLDERS:
                    new_value = pyip.inputStr(f"Enter {word.lower()}: ")
                    new_words.append(new_value)
                else:
                    new_words.append(word)
        wf.write("".join(new_words))


mad_libs("task_1.txt", "new_task_1.txt")

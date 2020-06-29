import pyinputplus as pyip

ADJECTIVE = "ADJECTIVE"
NOUN = "NOUN"
VERB = "VERB"


def mad_libs(file_for_read, file_for_write):
    """Read content from file, replace words of speech with entered ones and save outcomes to new file."""
    with open(file_for_read, "r") as rf:
        replaced_text = ""
        new_text = ""
        for line in rf:
            for index, character in enumerate(line):
                new_text += character
                if new_text.find(ADJECTIVE) != -1:
                    adjective_value = pyip.inputStr("Enter an adjective: ")
                    replaced_text += new_text.replace(ADJECTIVE, adjective_value)
                    new_text = ""
                if new_text.find(NOUN) != -1:
                    noun_value = pyip.inputStr("Enter a noun: ")
                    replaced_text += new_text.replace(NOUN, noun_value)
                    new_text = ""
                if new_text.find(VERB) != -1:
                    verb_value = pyip.inputStr("Enter a verb: ")
                    replaced_text += new_text.replace(VERB, verb_value)
                    new_text = ""
        final_text = replaced_text + new_text

        with open(file_for_write, "w") as wf:
            wf.write(final_text)
        print(final_text)


mad_libs("task_1.txt", "new_task_1.txt")

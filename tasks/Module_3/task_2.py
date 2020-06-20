import pytest

text = "Hello,Python"
text_separator = "Java"

VALUE_ERROR_MESSAGE = "empty separator"


def my_split(string, separator):
    final_list = list()
    new_string = ""
    for index, character in enumerate(string):
        new_string += character
        if separator == "":
            raise ValueError(VALUE_ERROR_MESSAGE)
        elif new_string.find(separator) != -1:
            final_list.append(new_string[0:len(new_string) - len(separator)])
            new_string = ""
    final_list.append(new_string)
    return final_list


# separator = ","
def test_split_with_comma():
    assert my_split(text, text_separator) == ['Hello', 'Python']


# separator = "o"
def test_split_with_existing_character():
    assert my_split(text, text_separator) == ['Hell', ',Pyth', 'n']


# separator = "th"
def test_split_with_existing_string():
    assert my_split(text, text_separator) == ['Hello,Py', 'on']


# separator = "Java"
def test_split_with_non_existing_string():
    assert my_split(text, text_separator) == ['Hello,Python']


# separator = ""
def test_split_with_empty_string():
    with pytest.raises(ValueError) as error:
        my_split(text, text_separator)
    assert VALUE_ERROR_MESSAGE in str(error.value)

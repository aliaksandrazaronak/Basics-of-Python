import pytest

text = "Hello,Python"

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


@pytest.mark.parametrize(
    "separator,expected",
    [(",", ['Hello', 'Python']),
     ("o", ['Hell', ',Pyth', 'n']),
     ("th", ['Hello,Py', 'on']),
     ("Java", ['Hello,Python'])])
def test_main_actions(separator, expected):
    assert my_split(text, separator) == expected


def test_split_with_empty_string():
    with pytest.raises(ValueError) as error:
        my_split(text, "")
    assert VALUE_ERROR_MESSAGE in str(error.value)


@pytest.mark.parametrize(
    "expected_text,separator",
    [("Python is good!", " "), ("Java is cool!", "is"), ("Python pytest pylint", "py")])
def test_compare_my_split_and_split_functions(expected_text, separator):
    assert my_split(expected_text, separator) == expected_text.split(separator)

import pytest

VALUE_ERROR_MESSAGE = "empty separator"


def my_split(string, separator):
    """Return a list of words divided with separator"""
    final_list = list()
    new_string = ""
    if separator == "":
        raise ValueError(VALUE_ERROR_MESSAGE)
    for index, character in enumerate(string):
        new_string += character
        if new_string.find(separator) != -1:
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
    text = "Hello,Python"
    assert my_split(text, separator) == expected


def test_split_with_empty_string():
    with pytest.raises(ValueError) as error:
        my_split("Empty String!", "")
    assert VALUE_ERROR_MESSAGE in str(error.value)


@pytest.mark.parametrize(
    "test,separator",
    [("Python is good!", " "), ("Java is cool!", "is"), ("Python pytest pylint", "py")])
def test_compare_my_split_and_split_functions(test, separator):
    assert my_split(test, separator) == test.split(separator)

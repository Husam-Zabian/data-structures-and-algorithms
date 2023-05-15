import pytest

from StackAndQueue.StackQueueBrackets import validate_brackets


def test_validate_brackets_balanced():
    assert validate_brackets("({})") == True
    assert validate_brackets("[(){}[]]") == True
    assert validate_brackets("") == True
    assert validate_brackets("(())[]{}{{}}") == True
    assert validate_brackets("[{()}]") == True
    assert validate_brackets("(([]{}))") == True

def test_validate_brackets_unbalanced():
    assert validate_brackets("({)}") == False
    assert validate_brackets("[({}])") == False
    assert validate_brackets("([)]") == False
    assert validate_brackets("(") == False
    assert validate_brackets(")") == False
    assert validate_brackets("{{}") == False
    assert validate_brackets("[") == False
    assert validate_brackets("]") == False    
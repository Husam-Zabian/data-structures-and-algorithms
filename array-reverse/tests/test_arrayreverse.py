import pytest

from Array.ArrayReverse import Array_reverse


def test_reverse_array():
    actual = Array_reverse([1, 2, 3, 4, 5])
    expected = [5, 4, 3, 2, 1]
    assert actual == expected


def test_reverse_array2():
    actual = Array_reverse([10, -62, 123, -4, 215])
    expected = [215, -4, 123, -62, 10]
    assert actual == expected
import pytest
from linkedList.linkedList.linkedList import LinkedList



@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    return linked_list

def test_k_greater_than_length(linked_list):
    assert linked_list.kthFromEnd(5) is None

def test_k_equals_length(linked_list):
    assert linked_list.kthFromEnd(3) is None

def test_not_positive_integer(linked_list):
    with pytest.raises(ValueError):
        linked_list.kthFromEnd(-1)

def test_linked_list_size_1():
    linked_list = LinkedList()
    linked_list.append(1)
    assert linked_list.kthFromEnd(0) == 1

def test_happy_path(linked_list):
    assert linked_list.kthFromEnd(0) == 3
    assert linked_list.kthFromEnd(2) == 1



def test_k_in_middle_of_list(linked_list):
    assert linked_list.kthFromEnd(1) == 2
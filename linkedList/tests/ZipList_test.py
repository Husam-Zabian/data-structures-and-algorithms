import pytest
from linkedList.linkedList.linkedList import LinkedList
from linkedList.linkedList.Ziplist import zip_two_lists

@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.append("item 1")
    linked_list.append("item 2")
    linked_list.append("item 3")
    return linked_list

def test_zip_lists_empty_lists():
    list1 = LinkedList()
    list2 = LinkedList()
    expected = LinkedList()
    assert zip_two_lists(list1, list2).to_string() == expected.to_string()

def test_zip_lists_first_list_empty(linked_list):
    list1 = LinkedList()
    assert zip_two_lists(list1,linked_list).to_string() == linked_list.to_string()

def test_zip_lists_second_list_empty(linked_list):
    list2 = LinkedList()
    assert zip_two_lists(linked_list,list2).to_string() == linked_list.to_string()

def test_zip_lists_same_length_lists(linked_list):
    list2 = LinkedList()
    list2.append("item 4")
    list2.append("item 5")
    list2.append("item 6")
    expected = LinkedList()
    expected.append("item 1")
    expected.append("item 4")
    expected.append("item 2")
    expected.append("item 5")
    expected.append("item 3")
    expected.append("item 6")
    assert zip_two_lists(linked_list, list2).to_string() == expected.to_string()

def test_zip_lists_different_length_lists():
    list1 = LinkedList()
    list1.append("item 1")
    list1.append("item 2")
    list1.append("item 3")
    list1.append("item 4")
    list2 = LinkedList()
    list2.append("item 5")
    list2.append("item 6")
    expected = LinkedList()
    expected.append("item 1")
    expected.append("item 5")
    expected.append("item 2")
    expected.append("item 6")
    expected.append("item 3")
    expected.append("item 4")


    assert zip_two_lists(list1, list2).to_string() == expected.to_string()
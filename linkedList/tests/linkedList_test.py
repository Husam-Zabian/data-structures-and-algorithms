import pytest
from linkedList.linkedList.linkedList import LinkedList

@pytest.fixture
def linked_list():
    linked_list = LinkedList()
    linked_list.insert("item 1")
    linked_list.insert("item 2")
    linked_list.insert("item 3")
    return linked_list

def test_linked_list_empty():
    linked_list_empty = LinkedList()
    actual = str(linked_list_empty)
    expected = "Empty LinkeList"
    assert actual == expected
    assert linked_list_empty.head is None

def test_linked_list_insert():
    linked_list_one_item = LinkedList()
    linked_list_one_item.insert("first item")
    actual = linked_list_one_item.head.value
    expected = "first item"
    assert actual == expected


def test_linked_list_insert_multiple(linked_list):
    actual = linked_list.head.value
    expected = "item 3"
    assert actual == expected

    actual = linked_list.head.next.value
    expected = "item 2"
    assert actual == expected

    actual = linked_list.head.next.next.value
    expected = "item 1"
    assert actual == expected

def test_linked_list_includes(linked_list):
    actual = linked_list.includes("item 1")
    expected = True
    assert actual == expected

    actual = linked_list.includes("item 4")
    expected = False
    assert actual == expected

def test_linked_list_to_string(linked_list):
    assert linked_list.to_string() == "{ item 3 } -> { item 2 } -> { item 1 } -> NULL"
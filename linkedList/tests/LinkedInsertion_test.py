import pytest
from linkedList.linkedList.linkedList import LinkedList

def test_append():
    linked_list = LinkedList()
    assert linked_list.to_string() == "NULL"
    
    linked_list.append("item 1")
    assert linked_list.to_string() == "{ item 1 } -> NULL"
    
    linked_list.append("item 2")
    assert linked_list.to_string() == "{ item 1 } -> { item 2 } -> NULL"
    
    linked_list.append("item 3")
    assert linked_list.to_string() == "{ item 1 } -> { item 2 } -> { item 3 } -> NULL"

def test_insert_before():
    linked_list = LinkedList()
    assert linked_list.to_string() == "NULL"
    
    linked_list.insert_before("item 3", "item 1")
    assert linked_list.to_string() == "NULL"
    
    linked_list.append("item 2")
    linked_list.insert_before("item 2", "item 1")
    assert linked_list.to_string() == "{ item 1 } -> { item 2 } -> NULL"
    
    linked_list.insert_before("item 1", "item 0")
    assert linked_list.to_string() == "{ item 0 } -> { item 1 } -> { item 2 } -> NULL"

def test_insert_after():
    linked_list = LinkedList()
    assert linked_list.to_string() == "NULL"
    
    linked_list.insert_after("item 3", "item 1")
    assert linked_list.to_string() == "NULL"
    
    linked_list.append("item 1")
    linked_list.insert_after("item 1", "item 3")
    assert linked_list.to_string() == "{ item 1 } -> { item 3 } -> NULL"
    
    linked_list.insert_after("item 3", "item 4")
    assert linked_list.to_string() == "{ item 1 } -> { item 3 } -> { item 4 } -> NULL"

    linked_list.insert_after("item 1", "item 2")
    assert linked_list.to_string() == "{ item 1 } -> { item 2 } -> { item 3 } -> { item 4 } -> NULL"

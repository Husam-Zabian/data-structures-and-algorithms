from StackAndQueue.Stack import Stack
import pytest

def test_push_one():
    stack = Stack()
    stack.push(1)
    assert stack.peek() == 1

def test_push_multiple():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.peek() == 3

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.peek() == 1

def test_empty_stack():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False
    stack.pop()
    assert stack.is_empty() == True

def test_peek_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.peek()

def test_pop_empty_stack():
    stack = Stack()
    with pytest.raises(Exception):
        stack.pop()
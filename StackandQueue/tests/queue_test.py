
from StackAndQueue.Node import Node
from StackAndQueue.Queue import Queue
import pytest

def test_enqueue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.peek() == 1

def test_enqueue_multiple():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.peek() == 1

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.peek() == 2

def test_empty_queue():
    queue = Queue()
    assert queue.is_empty() == True
    queue.enqueue(1)
    assert queue.is_empty() == False
    queue.dequeue()
    assert queue.is_empty() == True

def test_peek_empty_queue():
    queue = Queue()
    with pytest.raises(Exception):
        queue.peek()

def test_dequeue_empty_queue():
    queue = Queue()
    with pytest.raises(Exception):
        queue.dequeue()




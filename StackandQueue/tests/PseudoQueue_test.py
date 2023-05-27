
from StackAndQueue.PseudoQueue import PseudoQueue


def test_pseudo_queue_enqueue_1():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(20)
    pseudo_queue.enqueue(15)
    pseudo_queue.enqueue(10)
    pseudo_queue.enqueue(5)
    assert str(pseudo_queue) == "5 --> 10 --> 15 --> 20 -->  None"


def test_pseudo_queue_enqueue_2():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(5)
    assert str(pseudo_queue) == "5 -->  None"

def test_pseudo_queue_dequeue_1():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(15)
    pseudo_queue.enqueue(10)
    pseudo_queue.enqueue(5)
    assert pseudo_queue.dequeue() == 15
    assert str(pseudo_queue) == "5 --> 10 -->  None"

def test_pseudo_queue_dequeue_2():
    pseudo_queue = PseudoQueue()
    pseudo_queue.enqueue(20)
    pseudo_queue.enqueue(15)
    pseudo_queue.enqueue(10)
    pseudo_queue.enqueue(5)
    assert pseudo_queue.dequeue() == 20
    assert str(pseudo_queue) == "5 --> 10 --> 15 -->  None"
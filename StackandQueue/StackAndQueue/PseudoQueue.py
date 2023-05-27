from StackAndQueue.Stack import Stack

import pytest

class PseudoQueue:
    def __init__(self):
        """
        Initializes an empty PseudoQueue.
        """
        self.stack1 = Stack()
        self.stack2 = Stack()

    def __str__(self):
        """
        returns a string representation of the class PseudoQueue
        """
        if self.stack1.is_empty():
            return "Empty PseudoQueue"
        return str(self.stack1)
    def __repr__(self):
        """
        returns a string representation of the class PseudoQueue
        """
        if self.stack1.is_empty():
            return "Empty PseudoQueue"
        return str(self.stack1)
      
    def enqueue(self, value):
        """
        Adds a new node with the given value to the back of the queue using stack.

        Parameters:
        value (any): The value of the new node.
        """
        self.stack2.push(value)
        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
    
    def dequeue(self):
        """
        Removes and returns the value of the front node of the queue using stack.
        """
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise IndexError("Cannot dequeue from an empty PseudoQueue.")
    

        while not self.stack1.is_empty():
            self.stack2.push(self.stack1.pop())

        value = self.stack2.pop()

        while not self.stack2.is_empty():
            self.stack1.push(self.stack2.pop())
        
        return value
    
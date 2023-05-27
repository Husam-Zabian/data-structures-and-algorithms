from StackAndQueue.Node import Node
class Queue:
    """
    A class for the Queue data structure using a singly linked list.
    """
    def __init__(self):
        """
        Initializes an empty queue.
        """
        self.front = None
        self.back = None

    def __str__(self):
        """
        Returns a string representation of the queue.
        """
        output = ""
        if self.front is None:
            output = "Empty Queue LinkedList"
        else:
            current = self.front
            while current:
                output += f"{current.value} --> "
                current = current.next
            output += "None"
        return output

    def __repr__(self):
        """
        Returns a string representation of the class queue.
        """
        output = ""
        if self.front is None:
            output = "Empty Queue LinkedList"
        else:
            current = self.front
            while current:
                output += f"{current.value} --> "
                current = current.next
            output += "None"
        return output

    def enqueue(self, value):
        """
        Adds a new node with the given value to the back of the queue.

        Parameters:
        value (any): The value of the new node.
        """
        new_node = Node(value)
        if self.front is None:
            self.front = new_node
            self.back = new_node
        else:
            self.back.next = new_node
            self.back = new_node

    def dequeue(self):
        """
        Removes and returns the value of the front node of the queue.
        """
        if self.front is None:
            raise Exception("Queue is empty")
        else:
            value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.back = None
            return value

    def peek(self):
        """
        Returns the value of the front node of the queue without removing it.
        """
        if self.front is None:
            raise Exception("Queue is empty")
        else:
            return self.front.value

    def is_empty(self):
        """
        Returns True if the queue is empty, else False.
        """
        return self.front is None
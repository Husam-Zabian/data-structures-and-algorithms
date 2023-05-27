from StackAndQueue.Node import Node


class Stack:
    """
    A class for the stack data structure using a linked list.

    """
    def __init__(self):
        """
        Initializes an empty Stack.
        """
        self.top = None

    def __str__(self):
        """
        returns a string representation of the class Stack
        """
        output = ""
        if self.top is None:
            output = "Empty Stack LinkeList"
        else:
            current = self.top
            while(current):
                output += f'{current.value} --> '
                current = current.next
            output += " None"
        return output
    
    def __repr__(self):
        """
        returns a string representation of the class Stack
        """
        output = ""
        if self.top is None:
            output = "Empty Stack LinkeList"
        else:
            current = self.top
            while(current):
                output += f'{current.value} --> '
                current = current.next
            output += " None"
        return output   
    
    def push(self, value):
        """
        Adds a new node with the given value to the top of the stack.

        Parameters
        ----------
        value : node value.

        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        """
        Removes and returns the value of the top node of the stack.
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            value = self.top.value
            self.top = self.top.next
            return value
    
    def peek(self):
        """
        Returns The Value of the node located at the top of the stack
        """
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.top.value
    
    def is_empty(self):
        """
        Returns True if the stack is empty, Else False .

        """
        return self.top == None
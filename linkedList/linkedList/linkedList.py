from linkedList.linkedList.node import Node


class LinkedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            output += " None"
        return output
    
    def __repr__(self):
        output = ""
        if self.head is None:
            output = "Empty LinkeList"
        else:
            current = self.head
            while(current):
                output += f'{current.value} --> '
                current = current.next
            output += " None"
        return output
    
    def insert(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def includes(self, value):
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return True
            current_node = current_node.next
        return False
    
    def to_string(self):
        result = ""
        current_node = self.head
        while current_node:
            result += "{ " + str(current_node.value) + " } -> "
            current_node = current_node.next
        result += "NULL"
        return result

    def append(self, value):
        """
        Append a new node with the given value to the end of the linked list.
        Args:
            value: The value to be stored in the new node.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node


    def insert_before(self, value, new_value):
        """
        Insert a new node with the given new value before the node with the given value in the linked list.
        Args:
            value: The value of the node before which the new node should be inserted.
            new_value: The value to be stored in the new node.
        """
        new_node = Node(new_value)
        if self.head == None:
            return
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
        

    def insert_after(self, value, new_value):
        """
        Insert a new node with the given new value after the node with the given value in the linked list.
        Args:
            value: The value of the node after which the new node should be inserted.
            new_value: The value to be stored in the new node.
        """
        new_node = Node(new_value)
        if self.head == None:
            return
        current_node = self.head
        while current_node:
            if current_node.value == value:
                new_node.next = current_node.next
                current_node.next = new_node
                return
       linked-list-kth
            current_node = current_node.next

    def kthFromEnd(self,k):
        """
        Returns the value of the node that is k places from the tail of the linked list.
        
        Args:
            k (int): The distance from the end of the linked list.
        """
        if k < 0:
            raise ValueError("k cannot be negative")
    
        if self.head is None:
            return None
        
        current_node = self.head
        length = 0
        while current_node:
            length += 1
            current_node = current_node.next
        
        if k >= length:
            return None
        
        current_node = self.head
        for _ in range(1,length - k):
            current_node = current_node.next
            
        
        return current_node.value 

            current_node = current_node.next     


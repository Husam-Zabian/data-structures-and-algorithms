class Node:
    """
    A node class representing a single node in tree.
    """
    def __init__(self, value):
        """
        Initialize a new node with the given value.
         Attributes:
        - value: The value held by the node.
        - left: A reference to the left node in the tree.
        - left: A reference to the right node in the tree.
        """
        self.value = value
        self.left = None
        self.right = None
        
    def __str__(self):
        """
        Return a string representation of the node.
        """
        return f"Node with value = {self.value} "
    
    def __repr__(self):
        """
        Return a string representation of the node.
        """
        return f"Node with value = {self.value} "
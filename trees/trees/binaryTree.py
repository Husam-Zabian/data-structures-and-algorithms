class BinaryTree:
    def __init__(self):
        """
        Initialize an empty binary tree.
        """
        self.root = None

    def preorder_traversal(self, node):
        """
        Returns A list of values in a preorder traversal.
        """
        if node is None:
            return []
        result = [node.value]
        result += self.preorder_traversal(node.left)
        result += self.preorder_traversal(node.right)
        return result

    def inorder_traversal(self, node):
        """
        Returns A list of values in a inorder traversal.
        """
        if node is None:
            return []
        result = self.inorder_traversal(node.left)
        result.append(node.value)
        result += self.inorder_traversal(node.right)
        return result

    def postorder_traversal(self, node):
        """
        Returns A list of values in a postorder traversal.
        """
        if node is None:
            return []
        result = self.postorder_traversal(node.left)
        result += self.postorder_traversal(node.right)
        result.append(node.value)
        return result
    
    def find_maximum_value(self):
        """
        Returns the maximum value stored in the binary tree.
        """
        if self.root is None:
            raise ValueError("Binary tree is empty.")
        
        return self.recursive_Helper(self.root)

    def recursive_Helper(self, node):
        """
        Helper method to recursively find the maximum value in the binary tree.
        """
        if node is None:
            return float('-inf')

        max_value = node.value
        left_max = self.recursive_Helper(node.left)
        right_max = self.recursive_Helper(node.right)

        if left_max > max_value:
            max_value = left_max
        if right_max > max_value:
            max_value = right_max

        return max_value

    def __str__(self):
        """
        Return a string representation of the binary tree.
        """
        return ", ".join(str(value) for value in self.preorder_traversal(self.root))

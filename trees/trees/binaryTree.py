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

    def __str__(self):
        """
        Return a string representation of the binary tree.
        """
        return ", ".join(str(value) for value in self.preorder_traversal(self.root))

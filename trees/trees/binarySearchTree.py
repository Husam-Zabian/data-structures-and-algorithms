from trees.node import Node
from trees.binaryTree import BinaryTree


class BinarySearchTree(BinaryTree):
    def __str__(self):
        """
        Returns a string representation of the binary search tree.
        """
        return ", ".join(str(value) for value in self.preorder_traversal(self.root))
    def add(self, value):
        """
        Adds a new node with the given value to the binary search tree.
        """
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                elif value > current.value:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right
                else:
                    # Value already exists in the tree, do not add again
                    break

    def contains(self, value):
        """
        Returns True if the value exists in the tree, False otherwise.
        """
        if self.root is None:
            return False

        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False

    
import pytest
from trees.binaryTree import BinaryTree
from trees.node import Node
from trees.treeBreadthFirst import breadth_first

@pytest.fixture
def sample_binary_tree():
    """
    Creates a sample binary tree for testing.
    """
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.left.left.left = Node(6)
    tree.root.left.left.right = Node(7)

    return tree

def test_breadth_first_empty_tree():
    """
    Test breadth_first function with an empty tree.
    """
    tree = BinaryTree()
    assert breadth_first(tree) == []

def test_breadth_first(sample_binary_tree):
    """
    Test breadth_first function with a sample binary tree.
    """
    expected_output = [1, 2, 3, 4, 5, 6, 7]
    assert breadth_first(sample_binary_tree) == expected_output
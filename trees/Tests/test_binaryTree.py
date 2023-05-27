import pytest

from trees.binaryTree import BinaryTree
from trees.node import Node

def test_instantiating_empty_tree():
    tree = BinaryTree()
    assert tree.root is None

def test_instantiating_tree_with_single_root_node():
    tree = BinaryTree()
    tree.root = Node(1)
    assert tree.root.value == 1
    assert tree.root.left is None
    assert tree.root.right is None

def test_adding_left_and_right_child_to_node():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)

    assert tree.root.left.value == 2
    assert tree.root.right.value == 3
    assert tree.root.left.left is None
    assert tree.root.left.right is None
    assert tree.root.right.left is None
    assert tree.root.right.right is None

    
def test_preorder_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.preorder_traversal(tree.root) == [1, 2, 4, 5, 3]

def test_inorder_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.inorder_traversal(tree.root) == [4, 2, 5, 1, 3]

def test_postorder_traversal():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert tree.postorder_traversal(tree.root) == [4, 5, 2, 3, 1]

def test_str_representation():
    tree = BinaryTree()
    tree.root = Node(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    assert str(tree) == "1, 2, 4, 5, 3"
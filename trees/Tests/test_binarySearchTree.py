import pytest

from trees.binarySearchTree import BinarySearchTree

def test_add_left_and_right_child():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)

    assert tree.root.value == 5
    assert tree.root.left.value == 3
    assert tree.root.right.value == 7
    assert tree.root.left.left.value == 2
    assert tree.root.left.right.value == 4
    assert tree.root.right.left.value == 6
    assert tree.root.right.right.value == 8

def test_add_and_contains():
    tree = BinarySearchTree()
    tree.add(5)
    tree.add(3)
    tree.add(7)
    tree.add(2)
    tree.add(4)
    tree.add(6)
    tree.add(8)

    assert tree.contains(5) is True
    assert tree.contains(3) is True
    assert tree.contains(7) is True
    assert tree.contains(2) is True
    assert tree.contains(4) is True
    assert tree.contains(6) is True
    assert tree.contains(8) is True
    assert tree.contains(1) is False
    assert tree.contains(9) is False


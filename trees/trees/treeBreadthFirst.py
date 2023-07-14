# from StackAndQueue.StackAndQueue.node import Node
from StackandQueue.StackAndQueue.Queue import Queue
# from trees.trees.binaryTree import BinaryTree

def breadth_first(tree):
    """
    Performs a breadth-first traversal of the binary tree and returns a list of values in the order they were encountered.
    """
    if tree.root is None:
        return [] 

    result = []
    queue = Queue()  

    queue.enqueue(tree.root) 

    while not queue.is_empty():
        node = queue.dequeue()  
        result.append(node.value)  

        if node.left:
            queue.enqueue(node.left)  
        if node.right:
            queue.enqueue(node.right)  

    return result
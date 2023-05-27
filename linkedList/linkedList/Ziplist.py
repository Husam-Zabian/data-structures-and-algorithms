from linkedList.linkedList.linkedList import LinkedList

def zip_two_lists(LinkedList1, LinkedList2):
    """
    Returns A new linked list that is the result of zipping the two input lists together.
    
    Args:
    - LinkedList1: The first linked list .
    - LinkedList2: The second linked list.
    """
    # Check if either list is empty
    if not LinkedList1.head:
        return LinkedList2
    elif not LinkedList2.head:
        return LinkedList1
    
    # Zip the lists together
    current1 = LinkedList1.head
    current2 = LinkedList2.head
    while current1 and current2:
        temp1 = current1.next
        temp2 = current2.next
        current1.next = current2
        current2.next = temp1
        current1 = temp1
        current2 = temp2
    
    # Return the zipped list
    return LinkedList1
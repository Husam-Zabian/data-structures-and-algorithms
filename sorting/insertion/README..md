Code:

def insert(sorted_list, value):
    i = 0
    while value > sorted_list[i]:
        i += 1
    sorted_list.append(None)  # Extend the list by adding a None value at the end
    j = len(sorted_list) - 1
    while j > i:
        sorted_list[j] = sorted_list[j - 1]
        j -= 1
    sorted_list[i] = value


def insertion_sort(input_list):
    sorted_list = [input_list[0]]  # Initialize the sorted list with the first element
    for i in range(1, len(input_list)):
        insert(sorted_list, input_list[i])
    return sorted_list

from StackAndQueue.StackAndQueue.Stack import Stack

def validate_brackets(string):
    stack = Stack()
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}
    
    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if stack.is_empty() or bracket_pairs[stack.pop()] != char:
                return False
    
    return stack.is_empty()
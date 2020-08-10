from collections import deque
'''list = []
list.append('butts')
list.append('wut')
list.append('lmao')
list.append('yeet')
print(list.pop())
'''

'''stk = deque()
att = dir(stk)
print(att)

stk.append(89)
stk.append(9)
print(stk.pop())'''


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


# 1. Write a function in python that can reverse a string
# using stack data structure. Use Stack class from the tutorial.


def reverse_string(phrase):
    stack = Stack()
    rstr = ""

    for char in phrase:
        stack.push(char)

    while stack.size() != 0:
        rstr += stack.pop()

    print(rstr)


reverse_string("We will conquer COVID-19")


# 2. Write a function in python that checks if parenthesis in the string are balanced or not.
# Possible parentheses are "{}',"()" or "[]". Use Stack class from the tutorial.

def is_match(ch1, ch2):
    match_dict = {
        '(': ')',
        '{': '}',
        '[': ']'
    }

    return match_dict[ch1] == ch2


def is_balanced(phrase):
    stack = Stack()

    for char in phrase:
        if char == '(' or char == '{' or char == '[':
            stack.push(char)
        if char == ')' or char == '}' or char == ']':
            if stack.is_empty():
                return False
            if not is_match(stack.pop(), char):
                return False

    return stack.is_empty()


print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("((a+g))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

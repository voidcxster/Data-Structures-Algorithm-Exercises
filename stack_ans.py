import time
from collections import deque
from typing import Any

start_time = time.time()

class Stack:
    def __init__(self) -> None:
        self.container: deque = deque()
    
    def push(self, val: Any) -> None:
        self.container.append(val)
        
    def pop(self) -> Any:
        return self.container.pop()
    
    def peek(self) -> str:
        try:
            return self.container[-1]
        except IndexError:
            return ""
    
    def is_empty(self) -> bool:
        return len(self.container) == 0
    
    def size(self) -> int:
        return len(self.container)


parens: dict[str, str] = {
    '}': '{',
    ')': '(',
    ']': '['
}
openningParens: set[str] = {'{', '(', '['}

def is_balanced(s: str) -> bool:
    parenInString: Stack = Stack()
    isBalanced: bool = True
    for char in s:
        if char in openningParens: 
            parenInString.push(char)
        elif char in parens: # closing
            if parenInString.peek() == parens[char]:
                isBalanced = True
                parenInString.pop()
            else:
                return False
    if not parenInString.is_empty(): # open parens w/o closing
        isBalanced = False
    return isBalanced

def reverse_string(s: str) -> str:
    reversedStack: Stack = Stack()
    for char in s:
        reversedStack.push(char)
    reversedString: str = ""
    while not reversedStack.is_empty():
        reversedString += reversedStack.pop()
    return reversedString


print("1. Write a function in python that can reverse a string using stack data structure:")
print(reverse_string("We will conquere COVID-19"))

print("\n2. Write a function in python that checks if paranthesis in the string are balanced or not:")
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))

print("My program took", time.time() - start_time, "to run")
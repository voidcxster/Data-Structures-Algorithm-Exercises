from collections import deque

class Stack:
	def __init__(self):
		self.container = deque()
	
	def push(self,val):
		self.container.append(val)
		
	def pop(self):
		return self.container.pop()
	
	def peek(self):
		return self.container[-1]
	
	def is_empty(self):
		return len(self.container)==0
	
	def size(self):
		return len(self.container)

def reverse_string(s: str) -> Stack:
	reversedStack = Stack()
	for char in s:
		reversedStack.push(char)
	reversedString = ""
	while not reversedStack.is_empty():
		reversedString += reversedStack.pop()
	return reversedString

print(reverse_string("We will conquere COVID-19"))
from collections import deque
from typing import Any
import threading
import time

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)

    def front(self) -> Any:
        return self.buffer[-1]


orderQueue: Queue = Queue()

def place_order(o: list[Any]) -> None:
    for order in o:
        orderQueue.enqueue(order)
        time.sleep(0.5)

def serve_order() -> None:
    time.sleep(1)
    while True:
        try:
            print(orderQueue.dequeue())
        except IndexError:
            break
        time.sleep(2)

def print_binary(number: int) -> None:
    for i in range(1, number + 1):
        print(calc_bin(i))

def calc_bin(n: int) -> str:
    bq: Queue = Queue()
    place: int = 1
    while n >= place:
        place *= 2
    place = int(place / 2)
    while True:
        if n < place:
            place = int(place / 2)
            if place == 0:
                break
        if n - place >= 0:
            bq.enqueue("1")
            n -= place
        else:
            bq.enqueue("0")
    printStr: str = ""
    for itr in range(0, bq.size()):
        printStr += bq.dequeue()
    return printStr

def print_binary_solution(n: int) -> None:
    bq: Queue = Queue()
    bq.enqueue("1")

    for itr in range(n): # perform n - 1 times b/c 1 is already in the q
        front: str = bq.front()
        print(front)

        bq.enqueue(front + "0") 
        bq.enqueue(front + "1") 

        bq.dequeue()

print("1. Design a food ordering system where your python program will run two threads")
orders = ['pizza','samosa','pasta','biryani','burger']
t1 = threading.Thread(target = place_order, args = (orders,))
t2 = threading.Thread(target = serve_order)
t1.start()
t2.start()
t1.join()
t2.join()

print("\n")

print("2. Write a program to print binary numbers from 1 to 10 using Queue")
print_binary(10)
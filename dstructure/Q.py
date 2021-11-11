'''
             Queue
FIFO    first in first out

Queue implementation using Singly linked list
'''
from .LinkedList import SLL

class Queue(SLL):
    def __init__(self,iterables:list = None,capacity: int = None) -> None:
        self.capacity=capacity
        super().__init__(iterables)

    def __str__(self):
        return ', '.join(str(i.data) for i in self) if self.len!=0 else "Queue is empty"

    def __len__(self):
        return self.len
    
    def isFull(self):
        if self.capacity:
            if self.len==self.capacity:
                return True
            return False
    
    def isEmpty(self):
        if self.len==0:
            return True
        return False
    
    def push(self,value):
        if self.capacity:
            if self.isFull():
                return 'Sorry queue is full.'
            else:
                super().push(value)
        else:
            super().push(value)

    def pop_front(self):
        if self.isEmpty():
            return 'Queue is already empty'
        return super().pop(0)
    
    def peek(self):
        if not self.isEmpty():
            return self.head.data

    
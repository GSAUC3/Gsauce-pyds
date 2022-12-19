from typing import Any
from .linkedlist import DoublyLinkedList,LinkedList

# insertions are done from the REAR end
# deletions are done at the front
# enqueue() -> inserts an item at the end of the queue 
# dequeue() -> deletes an item from the front of the queue

class Queue(object):
    def __init__(self) -> None:
        pass

    def enqueue(self):
        pass 

    def dequeue(self):
        pass 

    

class Queue2(LinkedList):
    def __init__(self, *e) -> None:
        super().__init__(*e) 
    

    def __str__(self) -> str:
        s = ''
        for i in self:
            s += str(i.data)+','
        s =s.removesuffix(',')
        return f'Queue([{s}])'
    
    def __repr__(self) -> str:
        s = ''
        for i in self:
            s += str(i.data)+','
        s =s.removesuffix(',')
        return f'Queue([{s}], size={len(self)})'


    def enqueue(self,item:Any):
        # insertion
        super().append(item)
        

    def dequeue(self):
        super().remove(0) 
    
    def isempty(self):
        return True if len(self)==0 else False













from .DoublyLinkedList import DoublyLL


class dQ(DoublyLL):
    def __init__(self,iterables=None):
        super().__init__(iterables)
    
    def __len__(self):
        return self.len

    def __iter__(self):
        i=self.head
        while i:
            yield i.data
            i=i.next

    def __str__(self):
        return super().__str__()

    def pushback(self,val):
        super().push(val)
    
    def pushfront(self,val):
        super().push(val,0)
    
    def pop(self):
        return super().pop()
    
    def popfront(self):
        return super().pop(0)
    
    def insert(self,val,index: int):
        super().push(val,index)

    def extendright(self,iterables: list):
        for i in iterables:
            self.pushback(i)

    def extendleft(self,iterables: list):
        for i in iterables:
            self.pushfront(i)
        


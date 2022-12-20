from typing import Any
from dstructure.linkedlist import LinkedList
from dstructure.exceptions import EmptyDequeue
# insertions are done from the REAR end
# deletions are done at the front
# enqueue() -> inserts an item at the end of the queue 
# dequeue() -> deletes an item from the front of the queue
     
class Queue(LinkedList):
    def __init__(self, *e) -> None:
        '''
        e: accepts n number of objects

        >>> l = Queue(range(8))
        >>> print(l)
        Queue([0,1,2,3,4,5,6,7])
        ...
        >>> q = Queue([-1,2.0,3])
        >>> print(l)
        Queue([-1,2.0,3])
        ...
        >>> q = Queue(('a','b'))
        >>> print(q)
        Queue([a,b])
        ...
        >>> q = Queue(1,5,7,'s')
        >>> print(q)
        Queue([1,5,7,s])      
        '''
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
        return super().remove(0) 
    
    @property
    def isempty(self):
        return True if len(self)==0 else False




class Dequeue(LinkedList):
    def __init__(self,*e) -> None:
        super().__init__(*e)

    def __str__(self):
        s =''
        for i in self:
            s+= str(i.data) +','
        s =s.removesuffix(',')
        return f'Dequeue([{s}])'

    def __repr__(self):
        s =''
        for i in self:
            s+= str(i.data) +','
        s =s.removesuffix(',')
        return f'Dequeue([{s}],size = {len(self)})'

    def popback(self):
        '''
        removes element from the rear end of the Dequeue
        raises EmptyDequeue Error when the function is called
            on an empty dequeue
        '''
        if len(self)==0:
            raise EmptyDequeue
        return self.pop()

    def popfront(self):
        '''
        removes element from the front end of the Dequeue
        raises EmptyDequeue Error when the function is called
            on an empty dequeue
        '''
        if len(self)==0:
            raise EmptyDequeue
        return self.remove(0)

    def appendback(self,item):
        '''
        appends element at the rear end of the dequeue
        '''
        self.append(item)

    def appendfront(self,item):
        '''
        appends element at the front end of the dequeue
        '''
        self.insert(0,item)

    @property
    def isempty(self):
        return True if len(self)==0 else False






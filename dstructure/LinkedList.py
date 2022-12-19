'''Author: Rajarshi Banerjee'''

from typing import Optional,Any
from exceptions import EmptyList
from copy import deepcopy

class Node:
    def __init__(self,data:Optional[Any]=None,
                nextNode:Optional[Any]=None) -> None:
        self.data = data 
        self.next = nextNode
    
    def __repr__(self) -> str:
        return f'Node(data = {self.data})'
        
    def __str__(self) -> str:
        return f'Node(data = {self.data})'


class LinkedList(object):
    def __init__(self,*e) -> None:
        self.head = None
        self.tail = None 
        self.__size = 0

        if e:
            if type(e[0]) is range or list or tuple :
                for i in e[0]:
                    self.append(i)
            else: 
                for i in e:
                    self.append(i)

    @property    
    def size(self)->int:
        return self.__size
    
    def __len__(self):
        return self.__size

    def __iter__(self):
        i = self.head 
        while i:
            yield i 
            i = i.next

    def __str__(self) -> str:
        return 'LinkedList(['+', '.join(str(i.data) for i in self)+'])'
    
    def __repr__(self) -> str:
        return ' -> '.join(i.__str__() for i in self)
    

    def __getitem__(self,index):
        if isinstance(index,slice):
            if index.start<0:
                raise IndexError
            new = LinkedList()
            j = self.head
            i = 0
            __start = index.start if index.start is not None else 0
            __stop = index.stop if index.stop is not None else self.__size
            while j:
                if __start<=i<__stop:
                    new.append(j.data)
                j=j.next 
                i+=1
            return new
        elif isinstance(index,int):
            assert index>=0, 'index should be positive'
            if index>=self.__size:
                raise IndexError
            else:
                i=0
                j=self.head
                while i<index:
                    j=j.next
                    i+=1
                return j

    def __setitem__(self,index:int,data:Any)->None:
        assert index>=0 and type(index)==int, 'Index must be an integer >= 0'
        if index>=self.__size:raise IndexError 
        i = 0
        j = self.head 
        while i<index:
            j=j.next 
            i+=1 
        j.data = data 


    def append(self,data:Any)->None:
        self.__size+=1
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head 
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next

    def pop(self)->None:
        if self.head is not None:
            if self.head.next is None:
                self.head=None
                self.tail=None
            else:
                i = self.head 
                while i.next.next:
                    i = i.next
                i.next = None 
                self.tail = i
            self.__size-=1
        else:
            raise EmptyList
    
    def insert(self,at,data)->None:
        assert 0<=at<self.__size, 'index (at) should be an int between [ 0, len(list) )'
        i=0
        j = self.head
        new = Node(data)
        if at == 0:
            new.next = self.head 
            self.head = new 
            self.__size+=1
            return 
        else: 
            while i<at-1:
                j=j.next 
                i+=1
            new.next = j.next 
            j.next = new      
            self.__size+=1

         
    def remove(self,at)->None:
        assert 0<=at<self.__size, 'index (at) should be an int between [ 0, len(list) )'
        i=0
        j=self.head 
        if at ==0:
            self.head = self.head.next
            j.next = None 
            self.__size-=1
        else:
            while i<at-1:
                j=j.next 
                i+=1
            temp = j.next 
            j.next = temp.next
            temp.next=None 
            self.__size-=1
        

    def __add__(self,_o): 
        if isinstance(_o,LinkedList):
            new = deepcopy(_o)
            self.tail.next = new.head 
            self.tail = new.tail      
            self.tail.next=None
            self.__size+=len(_o)  
            del new
            return self
        else:
            raise ValueError
    
    def reverse(self)->None:
        past = None 
        present = self.head
        while present: 
            future = present.next 
            present.next = past 
            past = present 
            present = future 
            if future is not None:
                future = future.next 
        self.tail = self.head 
        self.head = past 
    
 

# circular singly linked list --------------  
class CircularList: 
    def __init__(self,*e) -> None:
        self.head = None 
        self.tail = None 
        self.__size = 0
        if e: 
            if type(e[0]) is range or list or tuple:
                for i in e[0]:
                    self.append(i)
            else:
                for i in e:
                    self.append(i)
        
    def __iter__(self):
        i = self.head 
        while i:
            yield i
            i = i.next  
            if i == self.head:
                break 

    def __len__(self):
        return self.__size

    def __repr__(self) -> str:
        s = ''
        for i in self:
            s += str(i.data) + ' '
        return s

    def append(self,data):
        self.__size +=1
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else: 
            self.tail.next = Node(data)
            self.tail = self.tail.next 
            self.tail.next = self.head 
            

    def pop(self):
        if len(self)<=0:
            raise EmptyList
        if self.tail is self.head and self.head is not None:
            self.__size-=1
            self.head=None
            self.tail=None
        else: 
            i = self.head 
            while i.next!= self.tail:
                i = i.next 
            temp = self.tail
            i.next = self.head 
            temp.next = None 
            del temp 
            self.tail = i 
            self.__size-=1
        
    
    def insert(self,index,data):
        assert 0<=index<self.__size , 'index should be an int between [0,len(list))'
        i =0 
        j = self.head 
        new = Node(data)
        if index == 0:
            new.next = self.head 
            self.head = new
            self.tail.next = self.head  
            self.__size+=1
        else:
            while i< index-1:
                j=j.next 
                i+=1 
            new.next = j.next 
            j.next = new 
            self.__size+=1

'''
Author : Rajarshi Banerjee
'''
from exceptions import *


# doubly linked list
class node:
    def __init__(self,data,prev=None,next=None):
        self.data = data 
        self.prev = None
        self.next = None
    
    def __repr__(self) -> str:
        return f'Node(data = {self.data})'
        
    def __str__(self) -> str:
        return f'Node(data = {self.data})'


class DoublyLinkedList(object):
    def __init__(self,*e) -> None:
        self.head = None
        self.tail = None
        self.__size:int = 0 
        if e:
            if type(e[0]) is range or list or tuple :
                for i in e[0]:
                    self.append(i)
            else: 
                for i in e:
                    self.append(i)       
                
    @property
    def size(self):
        return self.__size

    def __len__(self)->int:
        return self.__size 

    def __str__(self) -> str:
        s=''
        for i in self:
            s= s+ str(i.data) + ' '
        return f'DLList([{s.rstrip()}])'
    
    def __repr__(self) -> str:
        s = ''
        for i in self:
            s += i.__str__() + ' <=> '
        return s.removesuffix(' <=> ')

    def __iter__(self):
        i = self.head 
        while i:
            yield i 
            i=i.next 


    def __getitem__(self,index)->node:
        if not 0<=index <self.__size: raise IndexError
        i = self.head 
        j=0 
        while j<index:
            i=i.next 
            j+=1 
        return i 
        
    
    def __setitem__(self,index,data):
        if not 0<=index <self.__size: raise IndexError
        i = self.head 
        j=0 
        while j<index:
            i=i.next 
            j+=1 
        i.data = data 
        

    def append(self,data):
        if self.head is None: 
            self.head = node(data)
            self.tail = self.head 
            self.__size+=1
        else:
            temp = self.tail
            self.tail.next = node(data)
            self.tail = self.tail.next 
            self.tail.prev = temp
            self.__size+=1

    def pop(self):
        if self.head is self.tail and self.head is not None: 
             self.head = None 
             self.tail = None 
             self.__size-=1
        elif self.tail is not None: 
            temp = self.tail.prev 
            temp.next = None 
            self.tail.prev = None 
            self.tail = temp
            self.__size-=1 
        else:
            raise EmptyList

    def reverse(self):
        past = None 
        present =  self.head 
        while present: 
            past = present.prev 
            present.prev = present.next 
            present.next = past 
            present = present.prev

        self.head, self.tail = self.tail, self.head  
        

'''------------Circularly Doubly linked list--------------'''

        
class CircularlyDLL:
    def __init__(self,iterable=None):
        self.head = None
        self.tail = None
        self.len=0
        if iterable:
            for i in iterable:
                self.push(i)

    def __iter__(self):
        i=self.head
        while i:
            yield i
            i=i.next
            if i==self.head:
                break

    def __str__(self):
        return ' '.join(str(i.data) for i in self)

    def push(self,value,index=-1):
        if not self.head:
            n=node(value)
            n.next=n
            n.prev=n
            self.head=n
            self.tail=n
            self.len+=1
        else:
            if index==-1:
                self.tail.next=node(value,self.tail,self.head)
                self.tail=self.tail.next
                self.head.prev=self.tail
                self.len+=1
            elif index==0:
                self.head=node(value,self.tail,self.head)
                self.tail.next=self.head
                self.len+=1
            else:
                self.len+=1
                i=self.head
                j=0
                while j<index-1:
                    i=i.next
                    j+=1
                i.next=node(value,i,i.next)
                i.next.next.prev=i.next
                pass


    def pop(self,index=-1):
        if index >= self.len:
            print(' Enter a valid index!! INDEX IS 0 BASED')
            return 
        if not self.head:
            print('List is already empty')
        else:
            if index==-1 or index== self.len-1:
                self.len-=1
                temp=self.tail.data
                self.tail=self.tail.prev
                self.tail.next=self.head
                self.head.prev=self.tail
                return temp
            elif index==0:
                self.len-=1
                temp=self.head.data
                self.head=self.head.next
                self.head.prev=self.tail
                self.tail.next=self.head
                return temp
            else:
                self.len-=1
                i=self.head
                j=0
                while j<index-1:
                    i=i.next
                    j+=1
                temp=i.next.data
                i.next=i.next.next
                i.next.prev=i
                return temp

    def printList(self):
        if not self.head:
            print('List is empty :(')
        else:
            for i in self:
                print(i.data, end=', ')
        print('')

    def printreverse(self):
        if not self.head:
            print( ' List is empty :(')
        else:
            i=self.tail
            j=self.len
            while j:
                print(i.data,end=', ')
                i=i.prev
                j-=1
            print('')

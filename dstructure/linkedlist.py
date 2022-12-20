'''Author: Rajarshi Banerjee'''

from typing import Optional,Any
from dstructure.exceptions import EmptyList
from copy import deepcopy

class Node:
    def __init__(self,data:Any,
                nextNode:Optional[Any]=None) -> None:
        self.data = data 
        self.next = nextNode
    
    def __repr__(self) -> str:
        return f'Node(data = {self.data})'
        
    def __str__(self) -> str:
        return f'Node(data = {self.data})'


class LinkedList(object):
    def __init__(self,*e) -> None:
        """
        *e accepts three types of args 
        :type range:
        :type list:
        :type tuple:
        """
        self.head = None
        self.tail = None 
        self.__size = 0

        if e:
            if type(e[0]) is range or type(e[0]) is list or type(e[0]) is tuple:
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
            __start = index.start if index.start is not None else 0
            __stop = index.stop if index.stop is not None else self.__size
            if __start<0:
                raise IndexError
            new = LinkedList()
            j = self.head
            i = 0
            while j:
                if __start<=i<__stop:
                    new.append(j.data)
                j=j.next 
                i+=1
            return new
        elif isinstance(index,int):
            assert index>=0, 'index should be positive'
            if not 0<=index <self.__size: 
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
        if self.tail is not None:
            temp = self.tail.data
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
            return temp
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
            return j.data
        else:
            while i<at-1:
                j=j.next 
                i+=1
            temp = j.next 
            j.next = temp.next
            temp.next=None 
            self.__size-=1
            return temp.data
        

    def __add__(self,_o): 
        '''
        Concatenates two linkedlists into one 
        '''
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
            
#--------------------------------------------------------
# -------------------DOUBLY LINKED LIST------------------------------------------
#--------------------------------------------------------

class node:
    def __init__(self,data,prev=None,next=None):
        self.data = data 
        self.prev = prev
        self.next = next
    
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


    def __getitem__(self,index):
        if isinstance(index,slice):
            __start = index.start if index.start is not None else 0
            __stop = index.stop if index.stop is not None else self.__size
            if __start<0 or __stop<0:
                raise IndexError
            new = DoublyLinkedList()
            j = self.head
            i = 0
            while j:
                if __start<=i<__stop:
                    new.append(j.data)
                j=j.next 
                i+=1
            return new
        elif isinstance(index,int):
            assert index>=0, 'index should be positive'
            if not 0<=index <self.__size: 
                raise IndexError
            else:
                i=0
                j=self.head
                while i<index:
                    j=j.next
                    i+=1
                return j  
    
    
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


    def insert(self,at,data):
        pass 

    def remove(self,at):
        pass

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

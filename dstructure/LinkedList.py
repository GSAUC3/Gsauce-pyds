'''Author: Rajarshi Banerjee'''

class Node:
    def __init__(self,val=None,next_node=None):
        self.data=val
        self.next=next_node

class SLL:
    def __init__(self,listORtuple: list = None)->None:
        self.head=None
        self.tail=None
        self.len=0

        if listORtuple:
            for i in listORtuple:
                self.push(i)

    def __iter__(self):
        i=self.head
        while i:
            yield i
            i=i.next
        
    def __str__(self)->str:
        return f' a single linked list object.'

    def push(self,value,index=-1):
        if self.head is None:
            self.head=Node(value)
            self.len+=1
        else:
            if index==-1:
                i=self.head
                while i.next:
                    i=i.next
                i.next=Node(value,None)
                self.len+=1
            elif index==0:
                self.head=Node(value,self.head)
            else:
                self.len+=1
                i=0
                a=self.head
                while i<index-1:
                    a=a.next
                    i+=1
                
                a.next=Node(value,a.next)

    def printList(self)->None:
        if self.head is None:
            print('Linked List is empty')
            return
        else:

            print('Head-->',end=' ')
            for i in self:
                print(i.data,end=' --> ')
            print('Null')
    
    def pop(self,index=-1):
        if index>=self.len:
            print('index is out of range, INDEX IS 0 BASED')
        if not self.head:
            print('Linked list if already empty')
        else:
            if index==-1 or index==self.len-1:
                i=self.head
                while i.next.next: 
                    i=i.next 
                i.next=None
                self.len-=1  
            elif index==0:
                self.head=self.head.next
                self.len-=1
            else:
                self.len-=1
                i=self.head
                j=0
                while j<index-1:
                    i=i.next
                    j+=1
                i.next=i.next.next                
        
    def reverse(self):
        past=None
        while self.head:
            temp=self.head
            self.head=self.head.next
            temp.next=past
            past=temp
        self.head=past
    
    def get_node(self,node: int):
        if self.head is None:
            return 'List is empty :('
        elif node<=self.len:    
            j=1
            i=self.head
            while j< node:
                i=i.next
                j+=1
            return i.data
        else:
            return 'Index out of range, index should be less than list length/size.'


# circular singly linked list --------------  

class CircularList:
    def __init__(self,iterable: list = None):
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
        return " This is a circular singly linked list object"


    def push(self,value,index=-1):
        if not self.head:
            node=Node(value)
            node.next=node 
            self.head=node
            self.tail=node
            self.len+=1 
        else:
            if index==-1:
                i=1
                j=self.head
                while i<=self.len-1:
                    j=j.next
                    i+=1
                j.next=Node(value,self.head)
                self.tail=j.next
                self.len+=1 
            elif index==0:
                self.head=Node(value,self.head)
                self.tail.next=self.head
                self.len+=1
            else:
                j=self.head
                i=0
                while i<index-1:
                    j=j.next
                    i+=1
                j.next=Node(value,j.next)
                self.len+=1

    def pop(self,index=-1):
        '''return value needs to be added'''
        if index>=self.len:
            print('Enter a valid index, index is out of range! INDEX IS 0 BASED')
            return 
        if not self.head:
            print('List is empty. Duh!!')
        else:
            if index==-1 or index==self.len-1:
                i=self.head
                while i.next!=self.tail:
                    i=i.next
                i.next=self.head
                self.tail=i
                self.len-=1
            elif index==0:
                self.head=self.head.next
                self.tail.next=self.head
                self.len-=1
            else:
                j=0
                i=self.head
                while j<index-1:
                    i=i.next
                    j+=1
                i.next=i.next.next
                self.len-=1
                
    def printList(self):
        i=self.head
        print('Head',end='--> ')
        for i in self:
            print(i.data,end='--> ')
        print('Null')


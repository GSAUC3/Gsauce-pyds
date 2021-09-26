'''doubly linked list'''

class Node:
    def __init__(self,value,previous_node=None,next_node=None):
        self.data=value
        self.prev=previous_node
        self.next=next_node

class DoublyLL:
    def __init__(self,iterable: list = None):
        self.head=None
        self.tail=None
        self.len=0

        if iterable:
            for i in iterable:
                self.push(i)
    
    def __iter__(self):
        i=self.head
        while i:
            yield i
            i=i.next
    
    def __str__(self):
        return " A Doubly linked list object"
    
    def push(self,value,index=-1):
        if not self.head:
            n=Node(value)
            self.head=n
            self.tail=n
            self.len+=1
        else:
            if index==-1:
                self.len+=1
                self.tail.next=Node(value,self.tail)
                self.tail=self.tail.next
            elif index==0:
                self.head=Node(value,None,self.head)
                self.head.next.prev=self.head
                self.len+=1
            else:
                i=self.head
                j=1
                while j<index-1:
                    i=i.next
                    j+=1
                i.next=Node(value,i,i.next)
                i.next.next.prev=i.next
                self.len+=1
    
    def printList(self):
        if not self.head:
            print('List is empty :(')
        else:
            print('Head',end='--> ')
            i=self.head
            while i.next:
                print(i.data,end=' <==> ')
                i=i.next
            print(f'{self.tail.data} <-- Tail')

    def printReverse(self):
        if not self.head:
            print('List is empty :(')
        else:
            print('Tail',end='--> ')
            i=self.tail
            while i.prev:
                print(i.data,end=' <==> ')
                i=i.prev
            print(f'{self.head.data} <-- Head')
    
    def searchIndex(self,Node_value):
        if not self.head:
            return 'No point in searching, Create a list first. Its empty'
        i=0
        for j in self:
            if j.data==Node_value:
                return i
            i+=1
        return f'No such node with the given value {Node_value} exists'      
            
    def searchByIndex(self,index: int):
        if not self.head:
            return 'No point in searching, Create a list first. Its empty'
        i=1
        j=self.head
        while i<index:
            j=j.next
            i+=1
        return j.data
    
    def pop(self,index: int = -1):
        if index >= self.len:
            print(' Enter a valid index!! INDEX IS 0 BASED')
            return 
        if not self.head:
            print('Already empty')
        else:
            if index==-1 or index==self.len-1:
                self.len-=1
                temp=self.tail.data
                self.tail=self.tail.prev
                self.tail.next=None
                return temp
            elif index==0:
                self.len-=1
                temp=self.head.data
                self.head=self.head.next
                self.head.prev=None 
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
        return 'A Circularly Doubly Linked List object'

    def push(self,value,index=-1):
        if not self.head:
            n=Node(value)
            n.next=n
            n.prev=n
            self.head=n
            self.tail=n
            self.len+=1
        else:
            if index==-1:
                self.tail.next=Node(value,self.tail,self.head)
                self.tail=self.tail.next
                self.head.prev=self.tail
                self.len+=1
            elif index==0:
                self.head=Node(value,self.tail,self.head)
                self.tail.next=self.head
                self.len+=1
            else:
                self.len+=1
                i=self.head
                j=0
                while j<index-1:
                    i=i.next
                    j+=1
                i.next=Node(value,i,i.next)
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


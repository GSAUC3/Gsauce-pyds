class Node:
    def __init__(self,val=None,next_node=None):
        self.data=val
        self.next=next_node

class SLL:
    def __init__(self,listORtuple:list =None)->None:
        self.head=None
        self.tail=None
        self.len=0
        # self.value=listORtuple

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
    
    def delete(self,index=-1):
        if not self.head:
            print('Linked list if already empty')
        else:
            if index==-1:
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
    

class CSLL:
    def __init__(self):
        pass

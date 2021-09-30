'''Stack using list or dynamic arrays'''
from LinkedList import Node,SLL

class Stack:
    def __init__(self,*vals):
        self.l=[]
        self.top=-1
        for i in vals:
            self.push(i)
    
    def __str__(self):
        return ', '.join(map(str,self.l)) 
        
    def isEmpty(self):
        if not self.l:
            return True
        else:
            return False

    def peek(self):
        # peek operation returns the top of the stack of without deleting it
        if not self.l:
            return 'stack is empty'
        
        return self.l[self.top]
        


    def push(self,value):
        self.l.append(value)

    def pop(self):
        if self.l ==[]:
            return " Stack is already empty"            
        a=self.l.pop()
        return a

    def printStack(self):
        # x=self.l[::-1]
        print('_',end='')
        print('_\n_'.join(map(str,self.l[::-1])),end='')
        print('_') 
    
    def delete(self):
        self.l=[]
        return

'''implementation of stack using linked lists'''

class lstack(SLL):
    def __init__(self,x=None):
        super().__init__(x)
        pass

    def __str__(self):
        return ', '.join(str(i.data) for i in self) if self.len!=0 else "Stack is empty"

    def push(self, value):
        super().push(value)

    def peek(self):
        if self.head is None or self.len==0:
            return ' stack is empty'
        return self.tail.data

    def isEmpty(self):
        if self.len ==0:
            return True
        return False
    
    def pop(self):
        if self.len == 0:
            return 'Stack is empty'
        a=self.tail.data
        super().pop()
        return a

    def delete(self):
        self.head=None
    
            

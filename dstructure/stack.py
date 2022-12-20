'''Stack using list or dynamic arrays'''
from dstructure.linkedlist import LinkedList
from dstructure.exceptions import StackEmpty

class Stack:
    def __init__(self,*vals):
        self.l=[]
        self.top=-1
        for i in vals:
            self.push(i)
    
    def __str__(self):
        return ', '.join(map(str,self.l)) if not self.isEmpty() else "Stack is empty"
        
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
        print('_',end='')
        print('_\n_'.join(map(str,self.l[::-1])),end='')
        print('_') 
    
    def delete(self):
        self.l=[]
        return

'''implementation of stack using linked lists'''

class Stack2(LinkedList):
    def __init__(self, *e) -> None:
        super().__init__(*e) 
    

    def __str__(self):
        s = ''
        for i in self:
            s += str(i.data)+','
        s =s.removesuffix(',')
        return f'Stack([{s}])'

    def __repr__(self):
        s = ''
        for i in self:
            s += str(i.data)+','
        s =s.removesuffix(',')
        return f'Stack([{s}], size={len(self)})'

    @property
    def peek(self):
        return self.tail.data

    def push(self,item):
        super().append(item)
        
    def pop(self):
        if len(self)==0:
            raise StackEmpty
        else:
            return super().pop()
 
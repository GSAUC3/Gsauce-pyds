import math
from Q import Queue

from collections import deque

class btnode:
    def __init__(self,data,left_child=None,right_child=None):
        self.data=data
        self.left=left_child
        self.right=right_child

class binaryTree:
    def __init__(self,root=None) -> None:
        self.root=root
        self.size=0

    def __str__(self) -> str:
        l=[]
        self.__s(self.root,l)
        return ', '.join(l)
    
    def __s(self,node,l):
        if node:
            self.__s(node.left,l)
            l.append(str(node.data))
            self.__s(node.right,l)
    
    def insert():
        pass

    def height(self):
        return self.__height(self.root)
        
    def __height(self,node):
        if node is None:
            return 0
        return max(self.__height(node.left),self.__height(node.right))+1

    def Max(self):
        return self.__max(self.root)
    
    def Min(self):
        return self.__min(self.root)

    def __max(self,node):
        if node is None:
            return -math.inf
        return max(node.data,self.__max(node.left),self.__max(node.right))
    
    def __min(self,node):
        if node is None:
            return math.inf
        return min(node.data,self.__min(node.left),self.__min(node.right))
    
        
    def traversal(self,order:str ='pre'):
        '''For In order use: 'in'
        For Post order use: 'post'
        For Pre order use: 'pre' (default)
        '''
        if order=='pre':
            self.__preorder(self.root)
            print()
        if order=='post':
            self.__postorder(self.root)
            print()
        if order=='in':
            self.__inorder(self.root)
            print()
        
        if order=='level':
            if self.root is None:
                return 
            node=self.root
            q=Queue()
            q.push(node)
            while q:
                node=q.pop_front()
                print(node.data,end=' ')
                if node.left:
                    q.push(node.left)
                if node.right:
                    q.push(node.right)
                
            # if self.root is None:
            #     return 
            # node=self.root
            # q=deque()
            # q.append(node)
            # while q:
            #     node=q.popleft()
            #     print(node.data,end=' ')
            #     if node.left:
            #         q.append(node.left)
            #     if node.right:
            #         q.append(node.right)
                
        
    def __preorder(self,node):
            if node:
                print(node.data,end=' ')
                self.__preorder(node.left)
                self.__preorder(node.right)

    def __postorder(self,node):
            if node:
                self.__postorder(node.left)
                self.__postorder(node.right)
                print(node.data,end=' ')
                

    def __inorder(self,node):
            if node:
                self.__inorder(node.left)
                print(node.data,end=' ')
                self.__inorder(node.right)

    def __search(self,node,x):

        if node is None:
            return None
        elif node.data==x:
            return True
        elif self.__search(node.left,x)==True:
            return True
        else: 
            return self.__search(node.right,x)
            
    def search(self,value)->bool:
        return self.__search(self.root,value)
            
root=btnode(10,btnode(20),btnode(30,btnode(40),btnode(50)))
bt=binaryTree(root)
# bt.traversal('in')
bt.traversal('level')
# bt.traversal()
# print(bt.Max())
# print(bt.Min())
# print(bt.search(40))
# print(bt.height())


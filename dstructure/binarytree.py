import math
class btnode:
    def __init__(self,data,left_child=None,right_child=None):
        self.data=data
        self.left=left_child
        self.right=right_child

class binaryTree:
    def __init__(self,root=None) -> None:
        self.root=root
        self.size=0
    
    def insert():
        pass


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

root=btnode(10,btnode(20),btnode(30,btnode(40),btnode(50)))
bt=binaryTree(root)
bt.traversal('in')
bt.traversal('post')
bt.traversal()
print(bt.Max())
print(bt.Min())


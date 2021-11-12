import math
# from Q import Queue
from collections import deque


class btnode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left = left_child
        self.right = right_child


class binaryTree:
    def __init__(self, root=None) -> None:
        self.root = root
        self.size = 0

    def __str__(self) -> str:
        l = []
        self.__s(self.root, l)
        return ', '.join(l)

    def __s(self, node, l):
        if node:
            self.__s(node.left, l)
            l.append(str(node.data))
            self.__s(node.right, l)

    def height(self):
        return self.__height(self.root)

    def __height(self, node):
        if node is None:
            return 0
        return max(self.__height(node.left), self.__height(node.right))+1

    def Max(self):
        return self.__max(self.root)

    def Min(self):
        return self.__min(self.root)

    def __max(self, node):
        if node is None:
            return -math.inf
        return max(node.data, self.__max(node.left), self.__max(node.right))

    def __min(self, node):
        if node is None:
            return math.inf
        return min(node.data, self.__min(node.left), self.__min(node.right))

    def traversal(self, order: str = 'pre'):
        '''For In order use: 'in'
        For Post order use: 'post'
        For Pre order use: 'pre' (default)
        '''
        if order == 'pre':
            self.__preorder(self.root)
            print()
        if order == 'post':
            self.__postorder(self.root)
            print()
        if order == 'in':
            self.__inorder(self.root)
            print()

        if order == 'level':
            # if self.root is None:
            #     return
            # node=self.root
            # q=Queue()
            # q.push(node)
            # while q:
            #     node=q.pop_front()

            #     print(node.data,end=' ')
            #     if node.left:
            #         q.push(node.left)
            #     if node.right:
            #         q.push(node.right)

            if self.root is None:
                return
            node = self.root
            q = deque()
            q.append(node)
            while q:
                node = q.popleft()
                print(node.data, end=' ')
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

    def __preorder(self, node):
        if node:
            print(node.data, end=' ')
            self.__preorder(node.left)
            self.__preorder(node.right)

    def __postorder(self, node):
        if node:
            self.__postorder(node.left)
            self.__postorder(node.right)
            print(node.data, end=' ')

    def __inorder(self, node):
        if node:
            self.__inorder(node.left)
            print(node.data, end=' ')
            self.__inorder(node.right)

    def __search(self, node, x):

        if node is None:
            return None
        elif node.data == x:
            return True
        elif self.__search(node.left, x) == True:
            return True
        else:
            return self.__search(node.right, x)

    def search(self, value) -> bool:
        return self.__search(self.root, value)


class BST:
    def __init__(self, iterable: list = None) -> None:
        self.root = None
        if iterable:
            for i in iterable:
                self.insert(i)

    def __str__(self) -> str:
        l = []
        self.__s(self.root, l)
        return ', '.join(l)

    def __s(self, node, l):
        if node:
            self.__s(node.left, l)
            l.append(str(node.data))
            self.__s(node.right, l)

    def __in(self, node, x):
        if node is None:
            return btnode(x)
        elif x == node.data:
            return self.root
        elif x > node.data:
            if node.right is None:
                node.right = btnode(x)
            else:
                self.__in(node.right, x)

        else:
            if node.left is None:
                node.left = btnode(x)
            else:
                self.__in(node.left, x)

        return self.root

    def __search(self, node, x):
        if node is None:
            return False
        elif node.data == x:
            return True
        elif node.data > x:
            return self.__search(node.left, x)
        else:
            return self.__search(node.right, x)

    def insert(self, value):
        self.root = self.__in(self.root, value)

    def search(self, element):
        return self.__search(self.root, element)
    
    def floor(self,value):
        answer=None 
        i=self.root
        while i:
            if i.data==value:
                return f"Node: {i.data}"
            elif value<i.data:
                i=i.left
            else:
                answer=i.data
                i=i.right
        return f"Node: {answer}"

    def ceil(self,value):
        answer=None
        i=self.root
        while i:
            if i.data==value:
                return f"Node: {i.data}"
            elif value>i.data:
                i=i.right
            else:
                answer=i.data
                i=i.left
        return f"Node: {answer}"

    def isLeaf(self,node):
        if node:
            if node.right is None and node.left is None:
                return True
            return False


t = BST([10,20,5,51,50,-1])
print(t.ceil(40))

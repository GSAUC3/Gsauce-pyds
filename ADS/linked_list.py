from __future__ import annotations
from typing import Any


class SLLNode:
    def __init__(self, value: Any, next_node: SLLNode | None = None):
        self.val = value
        self.next = next_node

    def __str__(self):
        return f'Node({self.val})'

    def __repr__(self):
        return f'Node({self.val})'
    
    @property
    def dtype(self):
        return type(self.val)


class DLLNode:
    def __init__(
        self,
        value: Any,
        next_node: DLLNode | None = None,
        prev_node: DLLNode | None = None,
    ):
        self.val = value
        self.next = next_node
        self.prev = prev_node


class SLL:
    """
    Singly Linked List
    """
    def __init__(self, *args):
        self.__head = None
        self.__tail = None
        self.__size = 0 # total number of nodes 

        if args:
            for i in args:
                self.append(i)
        

    @property
    def size(self):
        return self.__size

    @property
    def head(self):
        return self.__head

    @property
    def tail(self):
        return self.__tail
    
    def __len__(self):
        return self.__size

    def __str__(self) -> str:
        return 'LinkedList(['+', '.join(str(i.val) for i in self)+'])'

    def __repr__(self):
        return ' -> '.join(i.__str__() for i in self)


    def __iter__(self):
        i = self.__head
        while i:
            yield i
            i = i.next


    def __getitem__(self, index):
        assert index>=0, 'index should be positive'
        if index>=self.__size:
            raise IndexError('Index is larger than length')
        i = 0
        curr = self.__head
        while i<index:
            curr = curr.next
            i+=1
        return curr


    def __add__(self, obj):
        if isinstance(obj,SLL):
            self.__size += obj.size
            self.__tail.next = obj.head
            self.__tail = obj.tail
            return self
        else:
            raise ValueError("can't concatenate lists of different types")

    def append(self, value: Any):
        if self.__size <1:
            self.__head = SLLNode(value = value)
            self.__tail = self.__head
        else:
            self.__tail.next = SLLNode(value=value)
            self.__tail = self.__tail.next
        self.__size+=1

    def add_front(self, value: Any):
        new_node = SLLNode(value = value, next_node = self.__head)
        self.__head = new_node

    def insert(self, index:int, value: Any):
        assert 0<=index<self.__size, 'index (at) should be an int between [ 0, len(list) )'
        if index <1:
            self.add_front(value)
        node_before_insertion = self.__getitem__(index-1)
        new_node = SLLNode(value,node_before_insertion.next)
        node_before_insertion.next = new_node
        self.__size+=1

class DLL:
    """
    Doubly Linked List
    """
    def __init__(self):...

from __future__ import annotations
from typing import Any
from copy import deepcopy


class SLLNode:
    def __init__(self, value: Any = 0, next_node: SLLNode | None = None):
        """Initialize a node in O(1) time."""
        self.val = value
        self.next = next_node

    def __str__(self):
        """Format the node in O(1) time, excluding value string conversion."""
        return f'Node({self.val})'

    def __repr__(self):
        """Format the node in O(1) time, excluding value string conversion."""
        return f'Node({self.val})'
    
    @property
    def dtype(self):
        """Return the value's type in O(1) time."""
        return type(self.val)


class DLLNode:
    def __init__(
        self,
        value: Any,
        next_node: DLLNode | None = None,
        prev_node: DLLNode | None = None,
    ):
        """Initialize a node in O(1) time."""
        self.val = value
        self.next = next_node
        self.prev = prev_node

    def __repr__(self):
        prev_val = self.prev.val if self.prev else None
        next_val = self.next.val if self.next else None
        return f"Node({prev_val}) <=> Node({self.val}) <=> Node({next_val})"

    def __str__(self):
        return f"{self.val}"

class SLL:
    """
    Singly Linked List
    """
    def __init__(self, *args):
        """Initialize from k values in O(k) time by appending each value."""
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
        """Deep-copy and concatenate m nodes in O(m) time, plus value-copy costs."""
        if not isinstance(obj,SLL):
            return NotImplemented        

        new = SLL()
        for i in self:
            new.append(i.val)
        for j in obj:
            new.append(j.val)
        return new


    def extend(self, new_list: SLL):
        if new_list is self:
            raise ValueError("cannot extend a list with itself")

        if new_list.head is None:
            return 
        

        if self.__head is None:
            ''' 
            these 3 are invariants which should stay
            constant throughout the program, 
            no matter what
            '''
            self.__head = new_list.head
            self.__tail = new_list.tail
            self.__size = len(new_list)
        else:
            self.__tail = new_list.head
            self.__tail = new_list.tail
            self.__size +=len(new_list)

        new_list.__head = None
        new_list.__tail = None
        new_list.__size = 0

        
    def append(self, value: Any):
        """Add a node at the tail in O(1) time using the tail reference."""
        if self.__size <1:
            self.__head = SLLNode(value = value)
            self.__tail = self.__head
        else:
            self.__tail.next = SLLNode(value=value)
            self.__tail = self.__tail.next
        self.__size+=1

    def add_front(self, value: Any):
        """Add a node at the head in O(1) time."""
        new_node = SLLNode(value = value, next_node = self.__head)
        self.__head = new_node

        if self.__tail is None:
            self.__tail = new_node

        self.__size+=1

    def insert(self, index:int, value: Any):
        """Insert at index in O(index) time; locating the predecessor traverses the list."""

        if  0<=index<=self.__size:
            raise IndexError('index (at) should be an int between [ 0, len(list)]') 
        
        if index <1:
            self.add_front(value)
        elif index == self.__size:
            self.append(value)
        else:
            node_before_insertion = self.__getitem__(index-1)
            new_node = SLLNode(value,node_before_insertion.next)
            node_before_insertion.next = new_node
            self.__size+=1

    def remove(self, index=0):
        """Remove at index in O(index) time; removing the tail delegates to pop."""
        if  0<=index<self.__size:
            raise IndexError('index (at) should be an int between [ 0, len(list)]') 
        
        if index == self.__size-1:
            return self.pop()

        if index ==0:
            temp = self.__head
            self.__head = self.__head.next
            if self.__size == 1:
                self.__tail = None

        else:
            prev_node = self.__getitem__(index-1)
            temp = prev_node.next
            prev_node.next = temp.next

        self.__size-=1

        return temp

    def pop(self):
        """Remove the tail in O(n) time because its predecessor must be found."""
        if self.__size ==0:
            raise IndexError("trying to pop from an empty list")

        temp_node = self.__tail
        
        if self.__size==1:
            self.__head = self.__tail = None
        else:
            second_last_node = self.__getitem__(self.__size-2)
            self.__tail = second_last_node
            self.__tail.next = None

        self.__size-=1
        return temp_node
            
    


class DLL:
    """
    Doubly Linked List
    """
    def __init__(self, *args):
        """Placeholder initializer; currently runs in O(1) time."""

        self.__head = None
        self.__tail = None
        self.__size = 0

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
        return ' <=> '.join(i.__str__() for i in self)

    
    def __iter__(self):
        i = self.__head
        while i:
            yield i
            i = i.next

    def append(self, value: Any):
        if self.__size <1:
            self.__head = DLLNode(value)
            self.__tail = self.__head
        else:
            self.__tail.next = DLLNode(value,prev_node = self.__tail)
            self.__tail = self.__tail.next

        self.__size+=1
    
    def pop(self):
        if self.__size==0:
            raise IndexError("trying to pop from an empty list")

        temp = self.__tail

        if self.__size == 1:
            self.__head = self.__tail = None
        else:
            self.__tail.prev.next = None
            dummy = self.__tail.prev
            self.__tail.prev = None
            self.__tail = dummy

        self.__size -=1
        return temp



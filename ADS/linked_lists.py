from __future__ import annotations
from abc import ABC, abstractmethod
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


class LinkedList(ABC):
    def __init__(self, *args):
        self._head = None
        self._tail = None
        self._size = 0

        if args:
            for i in args:
                self.append(i)

    @property
    def size(self):
        return self._size

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail
    
    def __len__(self):
        return self._size

    
    def __iter__(self):
        i = self._head
        for _ in range(self._size):
            yield i
            i = i.next

    def __getitem__(self, index:int):

        if not isinstance(index, int):
            raise TypeError("Index must be an integer")

        if index < 0 or index >= self._size:
            raise IndexError("Index out of range")

        curr = self._head
        for _ in range(index):
            curr = curr.next
        return curr


    def __add__(self, other):
        if type(self) is not type(other):
            return NotImplemented

        result = type(self)()

        for node in self:
            result.append(deepcopy(node.val))

        for node in other:
            result.append(deepcopy(node.val))

        return result

    @abstractmethod
    def append(self, value: Any) -> None:...

    @abstractmethod
    def pop(self):...


    @abstractmethod
    def insert(self, index: int = 0):...


    @abstractmethod
    def remove(self, index: int = 0):...

    @abstractmethod
    def extend(self, obj):...


class SLL(LinkedList):
    """
    Singly Linked List
    """
    def __init__(self, *args):
        """Initialize from k values in O(k) time by appending each value."""
        super().__init__(*args)    


    def __str__(self) -> str:
        return 'LinkedList(['+', '.join(str(i.val) for i in self)+'])'

    def __repr__(self):
        return ' -> '.join(i.__str__() for i in self)


    def extend(self, new_list: SLL):
        if new_list is self:
            raise ValueError("cannot extend a list with itself")

        if new_list.head is None:
            return 
        

        extended = self.__add__(new_list)
        self._head = extended.head
        self._tail = extended.tail
        self._size = len(extended)



        
    def append(self, value: Any):
        """Add a node at the tail in O(1) time using the tail reference."""
        if self._size <1:
            self._head = SLLNode(value = value)
            self._tail = self._head
        else:
            self._tail.next = SLLNode(value=value)
            self._tail = self._tail.next
        self._size+=1

    def add_front(self, value: Any):
        """Add a node at the head in O(1) time."""
        new_node = SLLNode(value = value, next_node = self._head)
        self._head = new_node

        if self._tail is None:
            self._tail = new_node

        self._size+=1

    def insert(self, value: Any, index:int = 0):
        """Insert at index in O(index) time; locating the predecessor traverses the list."""

        if  not 0<=index<=self._size:
            raise IndexError('index (at) should be an int between [ 0, len(list)]') 

        if index < 0:
            raise IndexError('Index must be positive')
        
        if index ==0:
            self.add_front(value)
        elif index == self._size:
            self.append(value)
        else:
            node_before_insertion = self.__getitem__(index-1)
            new_node = SLLNode(value,node_before_insertion.next)
            node_before_insertion.next = new_node
            self._size+=1

    def remove(self, index=0):
        """Remove at index in O(index) time; removing the tail delegates to pop."""
        if  not 0<=index<self._size:
            raise IndexError('index (at) should be an int between [ 0, len(list)]') 
        
        if index == self._size-1:
            return self.pop()

        if index ==0:
            temp = self._head
            self._head = self._head.next
            if self._size == 1:
                self._tail = None

        else:
            prev_node = self.__getitem__(index-1)
            temp = prev_node.next
            prev_node.next = temp.next

        self._size-=1

        return temp

    def pop(self):
        """Remove the tail in O(n) time because its predecessor must be found."""
        if self._size ==0:
            raise IndexError("trying to pop from an empty list")

        temp_node = self._tail
        
        if self._size==1:
            self._head = self._tail = None
        else:
            second_last_node = self.__getitem__(self._size-2)
            self._tail = second_last_node
            self._tail.next = None

        self._size-=1
        return temp_node
            
    
class DLL(LinkedList):
    """
    Doubly Linked List
    """
    def __init__(self, *args):
        """Placeholder initializer; currently runs in O(1) time."""
        super().__init__(*args)


    def __str__(self) -> str:
            return 'LinkedList(['+', '.join(str(i.val) for i in self)+'])'
    
    def __repr__(self):
        return ' <=> '.join(i.__str__() for i in self)


    def  __getitem__(self, index:int):
        # if index is <0 start from tail
        if not isinstance(index, int):
            raise TypeError(f"Expected an integer, but got {type(index).__name__}")

        
        if (abs(index) > self._size) or (index == self._size):
            raise IndexError('Index is out of bounds')
            
        
        if index>=0:
            curr = self._head
            i = 0
            while i < index:
                curr = curr.next
                i+=1
            return curr
        else:
            i = 1
            curr = self._tail
            while i<abs(index):
                curr = curr.prev
                i+=1
            return curr


    def append(self, value: Any):
        if self._size <1:
            self._head = DLLNode(value)
            self._tail = self._head
        else:
            self._tail.next = DLLNode(value,prev_node = self._tail)
            self._tail = self._tail.next

        self._size+=1
    
    def pop(self):
        if self._size==0:
            raise IndexError("trying to pop from an empty list")

        temp = self._tail

        if self._size == 1:
            self._head = self._tail = None
        else:
            self._tail.prev.next = None
            dummy = self._tail.prev
            self._tail.prev = None
            self._tail = dummy

        self._size -=1
        return temp


    def insert(self, value: Any, index:int=0):
        if not isinstance(index, int):
            raise TypeError(f"Expected an integer, but got {type(index).__name__}")

        #  only 0 based positive incides are allowed
        if not 0<=index<=self._size:
            raise IndexError('index (at) should be an int between [ 0, len(list)]') 

        if index == self._size:
            self.append(value)
            return

        if index == 0:
            new_node = DLLNode(value, next_node = self._head)
            if self._head is not None:
                self._head.prev = new_node
            self._head = new_node
            if self._tail is None:
                self._tail = new_node
            
        else:
            node_before_insertion = self.__getitem__(index-1)
            new_node = DLLNode(value,next_node = node_before_insertion.next,prev_node = node_before_insertion)
            node_before_insertion.next = new_node
            new_node.next.prev = new_node

        self._size+=1
        


    def remove(self, index:int = 0) -> DLLNode | None:
        if not isinstance(index, int):
            raise TypeError(f"Expected an integer, but got {type(index).__name__}")

        if not 0<=index<self._size:
            raise IndexError('index (at) should be an int between [ 0, len(list)]') 

        if self._size ==0:
            raise ValueError("List is already empty.")

        if (index == self._size-1) or (self._size == 1):
            return self.pop()

        if index == 0:
            temp = self._head
            self._head = self._head.next
            self._head.prev =  None
            temp.next = None
        else:
            prev_node = self.__getitem__(index-1)
            temp = prev_node.next
            
            prev_node.next = temp.next
            temp.next.prev = prev_node
            temp.next = None
            temp.prev = None

        self._size-=1
        return temp

    def extend(self, obj:DLL):
        if obj is self:
            raise ValueError("Cannot extend a DLL with itself.")

        if not (self._size == 0 and len(obj) ==0):
            # NOTE should we merge the two linked lists ?
            # self._tail.next = obj.head
            # obj.head.prev = self._tail
            # self._tail = obj.tail    

            for node  in obj:
                self.append(node.val)


class CircularSLL(LinkedList):
    def __init__(self, *args):
        super().__init__(*args)


    def append(self, value: Any):
        new  = SLLNode(value)
        if self._size == 0:
            new.next = new
            self._head = new
            self._tail = new
        else:
            new.next = self._tail.next
            self._tail.next = new
            self._tail = self._tail.next
        
        self._size+=1

    def insert(self, value:Any, index:int= 0):

        if  not 0<=index<=self._size:
            raise IndexError('index (at) should be an int between [ 0, len(list)]') 

        if index < 0:
            raise IndexError('Index must be positive')

        if index==0:
            if self._size == 0:
                self.append(value)
                return
            node = SLLNode(value, self._head)
            self._tail.next = node
            self._head = node

        elif index == self._size:
            self.append(value)
            return
        else:
            before_insertion_node = self.__getitem__(index-1)
            new_node = SLLNode(value, before_insertion_node.next)
            before_insertion_node.next = new_node
        self._size+=1

    def pop(self):
        if self._size == 0:
            raise IndexError("trying  to pop from an empty List")

        temp = self._tail
        if self._size == 1:
            self._head = self._tail = None
            self._size = 0
        else:
            self._tail = self.__getitem__(self._size-2)
            self._tail.next = self._head

            self._size-=1

        temp.next = None

        return temp
    
    def remove(self, index: int = 0):
        """Remove at index in O(index) time; removing the tail delegates to pop."""
        if  not 0<=index<self._size:
            raise IndexError('index (at) should be an int between [ 0, len(list)]') 
        
        if index == self._size-1:
            return self.pop()


        if index == 0:
            temp = self._head
            self._head = temp.next
            self._tail.next = self._head
        else:
            prev_node = self.__getitem__(index-1)
            temp = prev_node.next
            prev_node.next = temp.next


        temp.next = None
        self._size -=1
        return temp


    def extend(self, new_list: CircularSLL):
        if new_list is self:
            raise ValueError("cannot extend a list with itself")

        if not isinstance(new_list, CircularSLL):
            raise TypeError(f"Expected an CircularSLL object, but got {type(new_list).__name__}")

        if new_list.head is None:
            return 

        for node in new_list:
            self.append(deepcopy(node.val))
    
        # new_list._head = None
        # new_list._tail = None
        # new_list._size = 0




class CircularDLL(LinkedList):
    def __init__(self, *args):
        super().__init__(*args)

    def append(self, value: Any):
        new = DLLNode(value)
        if self._size == 0:
            new.next = new
            new.prev = new
            self._head = new
            self._tail = new
        
        self._size +=1
    def insert(self, value:Any, index:int= 0):
        pass
    
    def pop(self):
        pass

    def remove(self, index: int = 0):
        pass
    

        
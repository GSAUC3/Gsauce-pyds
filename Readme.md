# Data Structures for python
- Linked List
    - Singly Linked List
    - Circularly Singly Linked List
    - Doubly Linked List
    - Circularly Doubly Linked List


## Installation and pypi url
Latest Version : 0.0.4
```
pip install Gsauce-pyds
```

<a href="https://pypi.org/project/Gsauce-pyds/">Go to pypi/Gsauce-pyds url</a>

## How to use?

- Import the pacakge
```python
from dstructure import *
```
### Singly Linked List 

```python
from dstructure import *
L_list= SLL()
```
- Insert into linked list
```python
from dstructure import *
L_list= SLL()
L_list.push(1)
L_list.push(2)
L_list.push('word')
L_list.printList()

# Output:
# Head--> 1 --> 2 --> word --> Null

# push(value,index=-1) 
# index = -1 --> insert at the end of the list
# index = 0  --> insert at the beginning
# index = 5  --> insert element at location/index 5

# Note: 0 based index
```
- Deletion
```python
L_list.delete()  # this will delete the last element
L_list.delete(0) # will delete the first element
L_list.delete(4) # will delete element at index 4
```
Note: delete() takes one argument `index` which is by default set to -1, i.e. `delete(index=-1)` | -1 means it will delete the element from the end.

- list.len
```python
print(L_list.len) # will print the length of the linked list
```
- Reverse()
```python
L_list.reverse() # will reverse the linked list
# reverse() function returns NONE
```
- get_node()
```python
# To extract the data of a specific node
L_list.get_node(i) # to collect the ith node.data 
# returns the data of a specific index.
```

### Circularly singly linked list

Relevant Functions are given below:
```python
push(value,index)
'''Inserts values at given index | Default value of index is set to -1 
which means value will be appended at the end.
Indexing is 0 based.  | returns None'''

pop(index)
'''Default value of the index is set to -1 | returns the data after
deleting the specified node at given index.'''

printList()
'''Prints the entire list'''

#example

l=CircularList([1,2,3,4])
print(l.len) # returns the size of the list
l.printList()
#OUTPUT: 
# 4
# Head--> 1--> 2--> 3--> 4--> Null



```

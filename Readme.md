# Data Structures for python
- Linked List
    - Singly Linked List


## Installation and pypi url

```
pip install Gsauce-pyds
```

<a href="https://pypi.org/project/Gsauce-pyds/">Go to pypi/Gsauce-pyds url</a>

## How to use?

- Import the pacakge
```python
from dstructure import *
```
- Create a Singly Linked List object
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
L_list.delete()  # this will delete the element from the end
L_list.delete(0) # will delete the element from the beginning
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

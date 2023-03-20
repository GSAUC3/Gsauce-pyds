# Data Structures for python

## Installation
Latest Version : 1.0.0
python version needed: `>= 3.9`

```
pip install Gsauce-pyds
```
# Data Structures Implemented so far
Linked List | Doubly linked list | Stacks | Queue | dequeue


## Linked List
```python
from dstructure.linkedlist import LinkedList
l = LinkedList(range(8))
print(l)
# LinkedList([0, 1, 2, 3, 4, 5, 6, 7])

l.append('last')
print(l)
# LinkedList([0, 1, 2, 3, 4, 5, 6, 7, last])

print(len(l))
#9

print(l[0],l[5],l[8])
# Node(data = 0) Node(data = 5) Node(data = last)

print(l.head,l.tail)
# Node(data = 0) Node(data = last)

l[8]=8
print(l)
# LinkedList([0, 1, 2, 3, 4, 5, 6, 7, 8])

l.reverse()
print(l,'head: ',l.head,'tail: ',l.tail,sep='\n')
# LinkedList([8, 7, 6, 5, 4, 3, 2, 1, 0])
# head: 
# Node(data = 8)
# tail: 
# Node(data = 0)

print(l[:3],l[3:])
# LinkedList([8, 7, 6]) LinkedList([5, 4, 3, 2, 1, 0])

l.insert(0,'zero')
l.insert(3,'three')
print(l,len(l),l.head,l.tail,sep='\n')
# LinkedList([zero, 8, 7, three, 6, 5, 4, 3, 2, 1, 0])
# 11
# Node(data = zero)
# Node(data = 0)

l.remove(0)
l.remove(3)
print(l,l.head,l.tail,sep='\n')
# LinkedList([8, 7, three, 5, 4, 3, 2, 1, 0])
# Node(data = 8)
# Node(data = 0)

a = LinkedList('a b c'.split())
print(a)
a + l  # concatenation will overwrite the original list, in this case it's a
print(a)
# LinkedList([a, b, c])
# LinkedList([a, b, c, 8, 7, three, 5, 4, 3, 2, 1, 0])


print(len(a))
a.pop()
a.pop()
print(len(a))
# 12
# 10
```

`NOTE: to get the data of any LinkedList and DoublyLinkedList nodes use .data attribute | ex: l.head.data will return the actual value`
  
## Doubly Linked List

```python
from dstructure.linkedlist import DoublyLinkedList

l = DoublyLinkedList(range(4))
print(l)
# DLList([0 1 2 3])

l.append(4)
print(l,len(l))
# DLList([0 1 2 3 4]) 5

l.pop()
print(l)
# DLList([0 1 2 3])

print(l.head,l[0],l.tail,l[3],sep='\t')
# Node(data = 0)	Node(data = 0)	Node(data = 3)	Node(data = 3)

l.reverse()
print(l.head,l[0],l.tail,l[3],sep='\t')
# Node(data = 3)	Node(data = 3)	Node(data = 0)	Node(data = 0)

print(l.head.next,l.tail.prev)
# Node(data = 2) Node(data = 1)

print(l)
l[2]='two'
print(l)
# DLList([3 2 1 0])
# DLList([3 2 two 0])

print(l[:2],l[2:])
# DLList([3 2]) DLList([two 0])

```
## Stack
```python
from dstructure.stack import Stack2

s = Stack2(range(3))
print(s,len(s))
# Stack([0,1,2]) 3

s.push(3)
s.push(5)
print(s,len(s))
# Stack([0,1,2,3,5]) 5


s.pop()
print(s,len(s))
# Stack([0,1,2,3]) 4

print(s.peek)
# 3
```

## Queue
```python
from dstructure.queues import Queue

s = Queue(range(4))
print(s,len(s))
# Queue([0,1,2,3]) 4

s.enqueue('back')
s.enqueue('to back')
print(s,len(s))
# Queue([0,1,2,3,back,to back]) 6

s.dequeue()
print(s,len(s))
# Queue([1,2,3,back,to back]) 5

print(s.isempty)
# False

for _ in range(len(s)):
    s.dequeue()
print(s.isempty,len(s),s)
# True 0 Queue([])
```
## Dequeue 
```python

from dstructure.queues import Dequeue

s = Dequeue(range(4))
print(s,len(s))
# Dequeue([0,1,2,3]) 4

s.appendback('back')
s.appendfront('front')
print(s,len(s))
# Dequeue([front,0,1,2,3,back]) 6

s.popback()
s.popfront()
print(s,len(s))
# Dequeue([0,1,2,3]) 4

print(s.isempty)
for _ in range(len(s)):
    s.popback()
print(s.isempty,s,len(s))

# False
# True Dequeue([]) 0
```


## License

© 2021 Rajarshi Banerjee

This repository is licensed under the MIT license. See Licence for details.

## Link to package

<a href="https://pypi.org/project/Gsauce-pyds/"> pypi site </a>

***


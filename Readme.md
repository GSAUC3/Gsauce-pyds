# Data Structures for python
- ## Linked List
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
  
- ## Doubly Linked List
- ## Stack
- ## Queue
- ## Dequeue 

## Installation
Latest Version : 1.0.0
```
pip install Gsauce-pyds
```

## License

© 2021 Rajarshi Banerjee

This repository is licensed under the MIT license. See Licence for details.

## Link to package

<a href="https://pypi.org/project/Gsauce-pyds/"> pypi site </a>

***


import unittest
from dstructure.linkedlist import LinkedList
from dstructure.exceptions import *


class TestLinkedList(unittest.TestCase):

    def test_init(self):
        l = LinkedList(range(5))
        self.assertEqual(l.__str__(),'LinkedList([0, 1, 2, 3, 4])')
        self.assertEqual(len(l),5)
        l1 = LinkedList(0,1,2,3,4)
        self.assertEqual(l1.__str__(),'LinkedList([0, 1, 2, 3, 4])')
        l1 = LinkedList([0,1,2,3])
        self.assertEqual(l1.__str__(),'LinkedList([0, 1, 2, 3])')
        l1 = LinkedList((0,1,2,3,4))
        self.assertEqual(l1.__str__(),'LinkedList([0, 1, 2, 3, 4])')


    def test_headtaillen(self):
        l = LinkedList(range(5))
        self.assertEqual(l.head.data,0)
        self.assertEqual(l.head.next.data,1)
        self.assertEqual(l.tail.data,4)
        self.assertEqual(l.tail.next,None)
        self.assertEqual(len(l),5)
        l.append(5)
        self.assertEqual(len(l),6)
    
    def test_getsetslice(self):
        l = LinkedList(range(5))
        self.assertEqual(l[2].data,2)
        l[2]=20
        self.assertEqual(l[2].data,20)
        self.assertEqual(l[0].data,0)
        self.assertEqual(l[4].data,4)
        self.assertEqual(l.__str__(),'LinkedList([0, 1, 20, 3, 4])')
        self.assertEqual(l[:3].__str__(),'LinkedList([0, 1, 20])')
        self.assertEqual(l[3:].__str__(),'LinkedList([3, 4])')

    def test_reverse(self):
        l = LinkedList(range(5))
        l.reverse()
        self.assertEqual(l.__str__(),'LinkedList([4, 3, 2, 1, 0])')
        self.assertEqual(l.head.data,l[0].data)
        self.assertEqual(l.head.next.data,l[1].data)
        self.assertEqual(l.tail.data,0)
    
    def test_insertremove(self):
        l = LinkedList(range(5))
        l.insert(0,'front')
        self.assertEqual(l.__str__(),'LinkedList([front, 0, 1, 2, 3, 4])')
        l.insert(3,'three')
        self.assertEqual(l.__str__(),'LinkedList([front, 0, 1, three, 2, 3, 4])')
        self.assertEqual(l[3].data,'three')
        l.remove(0)
        self.assertEqual(l.__str__(),'LinkedList([0, 1, three, 2, 3, 4])')
        self.assertEqual(len(l),6)
        l.remove(3)
        self.assertEqual(l.__str__(),'LinkedList([0, 1, three, 3, 4])')
    
    def test_exceptions(self):
        l = LinkedList(1)
        l.pop()
        self.assertEqual(len(l),0)
      



if __name__ == '__main__':
    unittest.main()
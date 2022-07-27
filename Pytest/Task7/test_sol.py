from ctypes import pointer
from solution import Merge_sort
from solution import Node, LinkedList
import pytest
import random
import sys

class Test_small:
    def test_A(self):
        linked = LinkedList()
        linked.append(5)
        linked.append(3)
        linked.append(7)
        linked.append(1)
        linked.append(2)
        linked.append(6)
        linked.append(0)
        linked.append(4)
        head = linked.head
        answer = Merge_sort(head)
        for i in range(8):
            assert answer.data == i
            answer = answer.next

    def test_B(self):
        linked = LinkedList()
        linked.append(0)
        answer = Merge_sort(linked.head)
        assert answer.data == 0
        assert answer.next == None

    def test_C(self):
        linked = LinkedList()
        answer = Merge_sort(linked.head)
        assert answer == None
  
class Test_big:
    sys.setrecursionlimit(100000)
    def test_A(self):
        linked = LinkedList()
        A = [_ for _ in range(2001)]
        random.shuffle(A)

        for x in A:
            linked.append(x)

        answer = Merge_sort(linked.head)

        for i in range(len(A)):
            assert answer.data == i
            answer = answer.next

class Test_pointers:
    def test_A(self):
        linked = LinkedList()
        linked.append(5) # 0
        linked.append(3) # 1
        linked.append(7) # 2
        linked.append(9) # 3
        linked.append(1) # 4
        linked.append(2) # 5
        linked.append(6) # 6
        linked.append(0) # 7
        linked.append(8) # 8
        linked.append(4) # 9

        pointers_before = []
        curr_node = linked.head
        for i in range(10):
            pointers_before.append(curr_node.next)
            curr_node = curr_node.next
        pointers_before[0], pointers_before[7] = pointers_before[7], pointers_before[0]
        pointers_before[1], pointers_before[4] = pointers_before[4], pointers_before[1]
        pointers_before[2], pointers_before[5] = pointers_before[5], pointers_before[2]
        pointers_before[3], pointers_before[4] = pointers_before[4], pointers_before[3]
        pointers_before[4], pointers_before[9] = pointers_before[9], pointers_before[4]
        pointers_before[5], pointers_before[7] = pointers_before[7], pointers_before[5]
        answer = Merge_sort(linked.head)
        for i in range(10):
            assert answer.next == pointers_before[i]
'''0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9'''

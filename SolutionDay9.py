"""
This problem was asked by Microsoft.
Let's represent an integer in a linked list format by having each node represent a digit in the number. 
The nodes make up the number in reversed order.
For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5
is the number 54321.
"""

import numpy as np

class Node:
    def __init__(self, dataVal = None):
        self.dataVal = dataVal
        self.nextval = None

class LList:
    def __init__(self):
        self.headNode = Node()
    
    def append_data(self, data):
        new_node = Node(data)
        current = self.headNode
        while current.nextval is not None:
            current = current.nextval
        current.nextval = new_node
    
    def length_list(self):
        current = self.headNode
        total = 0
        while current.nextval is not None:
            total+=1
            current = current.nextval
        return total
    
    def printList(self):
        elements = []
        current_node = self.headNode
        while current_node.nextval is not None:
            current_node = current_node.nextval
            elements.append(current_node.dataVal)
        return elements

llist = LList()
llist.append_data(1)
llist.append_data(2)
llist.append_data(3)
llist.append_data(4)
llist.append_data(5)


def reverse_list(data):
    pp = []
    k = 0
    while k != data.length_list():
        pp.append(data.printList()[k])
        k+=1
    j = maxPP = len(pp)
    i = 0
    revList = []
    
    while i != maxPP:
        revList.append(pp[j-1])
        i+=1
        j-=1
    return revList
        
print(reverse_list(llist))


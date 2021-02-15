# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:12:18 2020

@author: giris
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
         self.head = None
    
    def insertEnd(self,newNode):
        if self.head is None:
            self.head = newNode
            
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode
            
    # function to print the linked LinkedList
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            
    def count_recursion(self, current, key, count):
        while current is not None:
            if current.data == key:
                count += 1
            current = current.next
            self.count_recursion(current, key, count)
        return count

    def recursion(self, key):
        if self.head is None:
            return
        count = 0
        return self.count_recursion(self.head, key, count)
    
    
linkedList = Linkedlist()
firstNode = Node(1)
linkedList.insertEnd(firstNode)

secondNode = Node(2)
linkedList.insertEnd(secondNode)

thirdNode = Node(1)
linkedList.insertEnd(thirdNode)

fourthNode = Node(4)
linkedList.insertEnd(fourthNode)

fifthNode = Node(5)
linkedList.insertEnd(fifthNode)

sixthNode = Node(5)
linkedList.insertEnd(sixthNode)

seventhNode = Node(5)
linkedList.insertEnd(seventhNode)
            
linkedList.printList() 
print()

print("5 is repeated {} times".format(linkedList.recursion(5)))        
print("1 is repeated {} times".format(linkedList.recursion(1)))

#print("5 is repeated {} times using recursive".format(linkedList.count_recursive(linkedList.head, 5)))   
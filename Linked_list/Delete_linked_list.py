# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:07:28 2020

@author: girish
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
            
    def deleteLinkedlist(self):
        current = self.head
        
        while current is not None:
            current_next = current.next
            del current.data
            current = current_next
        
        return current
    
    # function to print the linked LinkedList
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
        
    
linkedList = Linkedlist()
firstNode = Node(1)
linkedList.insertEnd(firstNode)

secondNode = Node(2)
linkedList.insertEnd(secondNode)

thirdNode = Node(3)
linkedList.insertEnd(thirdNode)

fourthNode = Node(4)
linkedList.insertEnd(fourthNode)

fifthNode = Node(5)
linkedList.insertEnd(fifthNode)
            
linkedList.printList()

print()
print("Deleting Linkedlist")
print(".")
print(".")
print(".")
linkedList.deleteLinkedlist()
print("Linked List Deleted")


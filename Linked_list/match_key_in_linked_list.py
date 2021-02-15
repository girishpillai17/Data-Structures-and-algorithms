# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 19:40:20 2020

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
            
    def findKey(self, key):
        
        # initialise current node at the head node
        currentNode = self.head
        
        # check till the next of current node is not None
        while currentNode.next is not None:
            # currentNode matches the key, return True else initialise the next of current to currentNode 
            if currentNode.data == key:
                print("{0} is present in the list".format(key))
            currentNode = currentNode.next
        
        print("{0} is not present in the list".format(key))
    
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

linkedList.findKey(10)

        
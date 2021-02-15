# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:53:13 2020

@author: girish
"""
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
        
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
    
    #insert at the beginnning
    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode
        
    #insert at given position
    def insertAt(self, newNode, position):
        
        #If invalid entry
        if position < 0 or position > self.listLength():
            print("Invalid entry")
            return
        
        #if position is 1, then it is insert at head so call headNode
        if position is 0:
            self.insertHead(newNode)
            return
        
        #if at between
        currentNode = self.head
        currentPosition = 0
        while True:
            if currentPosition == position:
                previousNode.next = newNode
                newNode.next = currentNode
                break
            previousNode = currentNode
            currentNode = currentNode.next
            currentPosition += 1
    
    #insert at the end of the node
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode
        
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            
    def deleteEnd(self):
        lastNode = self.head
        while lastNode.next is not None:
            previousNode = lastNode
            lastNode = lastNode.next
        previousNode.next = None
            

linkedList = Linkedlist()
firstNode = Node('Girish')
linkedList.insertEnd(firstNode)

secondNode = Node("Pillai")
linkedList.insertEnd(secondNode)

thirdNode = Node('Bhuvanendran')
linkedList.insertEnd(thirdNode)

headNode1 = Node('Mr')
linkedList.insertHead(headNode1)

headNode2 = Node('Rtr')
linkedList.insertEnd(headNode2)

linkedList.deleteEnd()

linkedList.printList()



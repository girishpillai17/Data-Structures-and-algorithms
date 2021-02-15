# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 21:39:41 2020

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
    
    def printList(self):
        currentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next
            
            
    def findNode_fromEnd(self, index):
        current = self.head
        
        length = 0
        while current is not None:
            current = current.next
            length += 1
        
            
        if index > length:
            print("Index greater than linked list")
            return
        
        temp = self.head
        for i in range(0, length - index):
            temp = temp.next
        print("the node at {} from end is {}".format(index, temp.data))
        
linkedList = Linkedlist()
firstNode = Node(8)
linkedList.insertEnd(firstNode)

secondNode = Node(5)
linkedList.insertEnd(secondNode)

thirdNode = Node(13)
linkedList.insertEnd(thirdNode)

fourthNode = Node(40)
linkedList.insertEnd(fourthNode)

fifthNode = Node(57)
linkedList.insertEnd(fifthNode)

linkedList.printList()


linkedList.findNode_fromEnd(1)
linkedList.findNode_fromEnd(2)
linkedList.findNode_fromEnd(3)
linkedList.findNode_fromEnd(4)
linkedList.findNode_fromEnd(5)
linkedList.findNode_fromEnd(6)
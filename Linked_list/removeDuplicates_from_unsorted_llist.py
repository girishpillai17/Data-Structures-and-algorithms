# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 22:07:53 2020

@author: giris
"""
# Python3 program to remove duplicate 
# nodes from a unsorted linked list  

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
            
    def get_previous_node(self, node):
        current = self.head
        while (current.next != node):
            current = current.next
        return current
    
    def removeNode(self, node):
        prev_node = self.get_previous_node(node)
        prev_node.next = node.next
            
        
    def removeDuplicates(self,linkedList):
        current = linkedList.head        
        while current is not None:
            data = current.data
            temp = current.next
            while temp is not None:
                if temp.data == data:
                    self.removeNode(temp)
                temp = temp.next
            current = current.next
            
            
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

linkedList.removeDuplicates(linkedList)
linkedList.printList() 
        
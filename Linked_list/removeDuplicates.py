# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 21:33:30 2020

@author: girish
"""

# Python3 program to remove duplicate 
# nodes from a sorted linked list  

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
        
    def removeDuplicates(self):
        temp = self.head
        
        if temp is None:
            return
        
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next.data = None
                temp.next = new
            else:
                temp = temp.next
        
        return self.head
    
    
linkedList = Linkedlist()
firstNode = Node(10)
linkedList.insertEnd(firstNode)

secondNode = Node(20)
linkedList.insertEnd(secondNode)

thirdNode = Node(20)
linkedList.insertEnd(thirdNode)

fourthNode = Node(30)
linkedList.insertEnd(fourthNode)

fifthNode = Node(35)
linkedList.insertEnd(fifthNode)

sixthNode = Node(40)
linkedList.insertEnd(sixthNode)

seventhNode = Node(45)
linkedList.insertEnd(seventhNode)

            
linkedList.printList() 
print()

linkedList.removeDuplicates() 
linkedList.printList()  
            
            
            
            
            
            
            
            
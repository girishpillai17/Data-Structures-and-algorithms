# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 23:57:48 2020

@author: giris
"""
# Python program to delete a node from linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Linkedlist:
    # Function to initialize head
    def __init__(self):
        self.head = None
        
    #create a linked list and add values to the end
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
          
            
    #Delete if the first occurence of the value when it matches with the data
    def deleteNode(self, value):
        # Store head node
        temp = self.head
        
        # If head node itself holds the key to be deleted
        if temp is not None:
            if temp.data == value:
                  self.head = temp.next
                  temp = None
                  return
          
        # Search for the key to be deleted, keep track of the  
        # previous node as we need to change 'prev.next        
        while temp is not None:
            if temp.data == value:
                break
            prev = temp
            temp = temp.next
            
        # if key was not present in linked list
        if temp == None:
            print("key not found")
            return
        
        # Unlink the node from linked list
        prev.next = temp.next
        temp = None
    
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
print("After Deleting, the linked list is :")
linkedList.deleteNode(3)
linkedList.printList()

print()
print("After Deleting, the linked list is :")
linkedList.deleteNode(4)
linkedList.printList()

print()
print("After Deleting, the linked list is :")
linkedList.deleteNode(8)
linkedList.printList()
        

        
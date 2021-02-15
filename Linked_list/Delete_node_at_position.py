# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:52:54 2020

@author: giris
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
        
class Linkedlist:
    # Function to initialize head
    def __init__(self):
        self.head = None
        
    def listLength(self):
        currentNode = self.head
        length = 0
        while currentNode is not None:
            length += 1
            currentNode = currentNode.next
        return length
        
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
    
    def deletNode(self, position):
        
        #If invalid entry
        if position < 0 or position > self.listLength():
            print("Invalid entry")
            return
        
        temp = self.head
        
        # if postion is 0 i.e head node
        if position == 0:
            self.head == temp.next
            temp.data = None
            return
        
        
        for i in range(position):
            prev = temp
            temp = temp.next
            if temp is None:
                break
            
        # if temp is None return the Linked list
        if temp == None:
            return
        
        # Assign the next of previous to next of temp and Delete the temp node
        prev.next = temp.next
        temp.data = None
        
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
linkedList.deletNode(4)
linkedList.printList()


        
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:00:53 2020

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
            
    def ifLoop(self):
        pointer_1 = self.head
        pointer_2 = self.head
        
        while(pointer_1 and pointer_2 and pointer_2.next is not None):
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next
            
            if pointer_1 == pointer_2:
                print("There is a loop")
                return
        
        print("loop not found")
            
linkedList = Linkedlist()
firstNode = Node(10)
linkedList.insertEnd(firstNode)

secondNode = Node(15)
linkedList.insertEnd(secondNode)

thirdNode = Node(4)
linkedList.insertEnd(thirdNode)

fourthNode = Node(20)
linkedList.insertEnd(fourthNode)

fifthNode = Node(5)
linkedList.insertEnd(fifthNode)

sixthNode = Node(2)
linkedList.insertEnd(sixthNode)

seventhNode = Node(2)
linkedList.insertEnd(seventhNode)

# Create a loop for testing 
linkedList.head.next.next.next.next.next.next.next = linkedList.head.next.next.next

#linkedList.printList()

linkedList.ifLoop()


            
            

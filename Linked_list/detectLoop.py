# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 23:48:18 2020

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
        current = self.head
        
        hashNodes = set()
        
        while current:
            if current.data in hashNodes:
                return True
            
            hashNodes.add(current)
            current = current.next
            
        return False
        
        
    
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

            
linkedList.printList() 
print()

linkedList.head.next.next.next.next = linkedList.head;

if( linkedList.ifLoop()): 
    print ("Loop found") 
else : 
    print ("No Loop") 


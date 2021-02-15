# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:16:39 2020

@author: girish
"""

class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linkedlist:
    def __init__(self):
         self.head = None
         self.counter = 0
    
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
            
    def count(self, search_key):
        current = self.head
        
        # Counts the no . of occurrences of a node 
        # (search_for) in a linked list (head) 
        count = 0
        while current is not None:
            if current.data == search_key:
                count += 1
            current = current.next
           
        return count
    
    # Method 2 - Recursive
    def count_recursive(self, head, search_key):
        
        #Base case:
        if head is None:
            return self.counter
                
            
        if head.data == search_key:
            self.counter = self.counter + 1
            
        return self.count_recursive(head.next, search_key)

linkedList = Linkedlist()
firstNode = Node(1)
linkedList.insertEnd(firstNode)

secondNode = Node(2)
linkedList.insertEnd(secondNode)

thirdNode = Node(1)
linkedList.insertEnd(thirdNode)

fourthNode = Node(4)
linkedList.insertEnd(fourthNode)

fifthNode = Node(5)
linkedList.insertEnd(fifthNode)

sixthNode = Node(5)
linkedList.insertEnd(sixthNode)

seventhNode = Node(5)
linkedList.insertEnd(seventhNode)
            
linkedList.printList() 
print()

print("5 is repeated {} times".format(linkedList.count(5)))        
print("1 is repeated {} times".format(linkedList.count(1)))

print("5 is repeated {} times using recursive".format(linkedList.count_recursive(linkedList.head, 5)))        

        
        
        
        
        
        
        
        
        
        
        
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 19:31:19 2020

@author: girish
"""

class Node:
    def __init__(self):
        self.data = None
        self.next = None
    
    #set data field
    def set_data(self,data):
        self.data = data
        
    #get the data
    def get_data(self):
        return self.data
    
    #set the next field
    def set_next(self,next):
        self.next = next
        
    #get the next field
    def get_next(self):
        return self.next
    
    #check if this is the last field if not then return next field
    def has_next(self):
        return self.next != None



#Insert data at the begining
def insertBegining(self, data):
    newNode = Node()
    newNode.set_data(data)
    
    if self.length == 0:
        self.head = newNode
    
    else:
        newNode.set_next(self.head)
        self.head = newNode
    
    self.length += 1

    
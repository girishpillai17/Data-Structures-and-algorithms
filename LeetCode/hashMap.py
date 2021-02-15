# Program to implement HashTable in python

class HashTable:
    def __init__(self):
        self.size = 100                             #Size of the HashMap/Hashtable
        self.arr = [None for i in range(self.size)] #initializing the array with Null values first and then values will be added accordingly

    def getHash(self, key):
        hash_val = 0                   # Initializing hash value with 0
        for char in key:               # Spliting the string to get each character   
            hash_val += ord(char)      # Fiding the ASCII value of each character and adding it to hash
        return hash_val % self.size    # Taking the mod by finding out the remainder when divided by the size of the array

    def addValue(self, key, value):    # Function to add value in the array/Table
        hash_val = self.getHash(key)   # Get the Hash_value/Index of the key
        self.arr[hash_val] = value     # Value will be added to the position hash_value(number) to the array

    def getValue(self, key):           # Function to get a vaue which is already in the table
        hash_value = self.getHash(key) # Get the Hash_value/Index of the key
        return self.arr[hash_value]    # Return the value stored in that key
    
    def deletValue(self, key):         # Function to delete vaue which is already in the table
        hash_value = self.getHash(key) # Get the Hash_value/Index of the key
        self.arr[hash_value] = None    # Replace the value with None

t = HashTable()
t.addValue("march 6", 130)
print(t.arr)
print(t.getValue("march 6"))
t.addValue("march 6", 140)
print(t.arr)
print(t.getValue("march 6"))

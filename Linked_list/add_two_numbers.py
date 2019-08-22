class Node:
    def __init__(self, data):
        self.data = data   #given input data
        self.next = None   #initialize next node with None, will be filled later


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def addTwoLists(self, first, second):
        prev = None
        temp = None
        carry = 0

        while (first is not None or second is not None):

            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            sum = carry + fdata + sdata

            carry = 1 if sum > 10 else 0

            sum = sum if sum < 10 else sum%10

            temp = Node(sum)

            if self.head = None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

            
        if carry > 0:
            temp.next = Node(carry)
    
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

        
first = Linked_list()
second = Linked_list()

first.insert_head(6)
first.insert_head(4)
first.insert_head(9)
first.insert_head(5)
first.insert_head(7)
print ("First List is ", first.printList()) 

second.insert_head(4)
second.insert_head(8)
print ("\nSecond List is ", second.printList(0))

res = LinkedList() 
res.addTwoLists(first.head, second.head) 
print("\nResultant list is ", res.printList()) 

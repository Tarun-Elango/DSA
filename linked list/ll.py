# linked list 
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        # the tail has next as none
    def printll(self):
        printVal = self.head
        while printVal is not None:
            print(printVal.data)
            printVal= printVal.next

    def insertLLBegin(self, newValue):
        newNode = Node(newValue) # create a new node with the new value
        newNode.next = self.head # add current head to new node's next
        self.head = newNode # set current head as new node

    def insertLLatEnd(self, newValue):
        newNode=Node(newValue) # create a new node with the new value
        if self.head is None:
            self.head = newNode
            return
        currentval= self.head # take current head
        while(currentval.next): #iterate the list
            currentval= currentval.next
        
        #currentVal has the last value
        currentval.next = newNode

    def insertllBetween(self, after, new): # add new after 'after'
        if(after is not None):
            newNode = Node(new) # create new node
            newNode.next =after.next # set new node's next as old after node's next
            after.next = newNode # set old after node's next as new node'
    
    def removeitemLL(self, item):
        if(item is not None):
            # find the node that has nextval as item
            head = self.head
            if(head == item): # when head is the item to be removed
                self.head = head.next  # set the new head as the old heads next
                head = None
                return
            
            while head is not None: # find the item
                if (head == item):
                    break
                prev = head
                head = head.next

            if(head == None):
                return
        
            prev.next = head.next
            head = None



list = LinkedList()
list.head = Node("hello")
two = Node("your")
three = Node('highness.')

#join
list.head.next =two
two.next = three

list.printll()
#list.removeitemLL(three)
#list.printll()
#list.insertllBetween(two,'sweet')
#list.printll()




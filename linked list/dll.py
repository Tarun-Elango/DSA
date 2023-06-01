# doubly
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None

    #add function
    def addval(self, data):  # at the beginning
        newNode = Node(data)
        newNode.next = self.head
        if self.head is not None: # when empty
            self.head.prev = newNode
        self.head = newNode
    
    def printll(self):
        head = self.head
        while head is not None:
            print(head.data)
            head = head.next

    # insert at pos
    def insertat(self, data, pos):
        if pos.data is None:
            return
        newNode = Node(data) #create a new node
        newNode.next = pos.next # set new node next to old position.next
        pos.next = newNode # set old position.next to newnode
        newNode.prev=pos # set new node prev to old pos

        if newNode.next is not None:
            newNode.next.prev = newNode # if next to newnode is there, set its prev to newNode

    def insertAtEnd(self,data):
        newNode = Node(data)
        newNode.next = None # as this is the last
        if self.head is None:
            newNode.prev = None
            self.head = newNode
            return
        findLast = self.head
        while findLast.next is not None:
            findLast = findLast.next

        # last has the last one
        findLast.next = newNode
        newNode.prev = findLast
        return


dll= DoublyLL()
dll.addval(1)
dll.addval(2)
dll.addval(3)
dll.printll()
#dll.insertat(20, dll.head.next)
#dll.printll()

dll.insertAtEnd(0)
dll.printll()
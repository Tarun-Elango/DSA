class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class cll:
    def __init__(self):
        self.head = None

    #add value same as ll, but last.next = first
    
    def addAtStart(last, data): # need last as well as data
        if last is None: 
            return
        
        newNode = Node(data)

        newNode.next = last.next
        last.next = newNode

        return
    
    def addAtEnd(last, data): 
        newNode = Node(data)
        newNode.next = last.next
        last.next = newNode  # set the newnode to point to first, and old last to point to newnode

        # now the newNode is actually the start
        # therefore, point the previous last as the newNode
        last = newNode

        return

    def addAtPos(last, pos, data):  #insert after data
        if last is None:
            return None
        
        temp = last.next # the start

        while (temp != last):
            if temp ==data:
                # insert node after 'data', then if it is last (it becomes new start), therefore set the current last to newNode
                newNode = Node(data)
                newNode.next = temp.next
                temp.next = newNode

                # if we are at the end of the list then point the previos last to newnode
                if (temp == last):
                    last = newNode
            temp = temp.next


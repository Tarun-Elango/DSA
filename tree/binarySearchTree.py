# binary search tree
# one root node
# every other node has a parent, and at most 2 children, left < right

class Node:
    def __init__(self,val):
        self.val = val
        self.rightchild = None
        self.leftchild = None
    
class BSTREE:
    def __init__(self):
        self.root= None

    def get_root(self):
        return self.root
    
    def add(self,val): # add the value to parent 'node'
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return
        
        current = self.root
        while True:
            if val < current.val:
                if current.leftchild is None:
                    current.leftchild = newNode
                    return 
                current = current.leftchild
            else:
                if current.rightchild is None:
                    current.rightchild = newNode
                    return 
                current = current.rightchild

    def find(self,data):
        current = self.root
        while current is not None:
            if current.val == data:
                return True
            elif current.val < data:
                current= current.rightchild
            else:
                current= current.leftchild
        return False

# Create a binary tree
tree = BSTREE()

# Insert elements into the tree
tree.add(5)
tree.add(3)
tree.add(7)
tree.add(1)
tree.add(4)
tree.add(6)
tree.add(8)

# Search for an element in the tree
result = tree.find(4)
if result:
    print("Element found!")
else:
    print("Element not found!")

# hash table needs size(number of elements inserted), capacity - size of internal array, 
# buckets - the internal arrays, storing each element in the bucket based on the key
# buckets are meant to keep track of keys, each bucket is linked to the hashed key. if repeated stored as linked list
initialCapacity = 50 # prime number


class Node:
    def __init__(self, key, value):
        self.key = None
        self.value = None
        self.next = None # part of linked list, as each bucket actually has a linked list (seperate chaining for collision resolution)

    

class Hashtable:
    def __init__(self):
        self.size = 0
        self.capacity = initialCapacity
        self.buckets = [None] * self.capacity

    # add the hash, insert .. values in hashtable class
    def hash(self, key):
        sum=0
        for index, c in enumerate(key):
            # Add (index + length of key) ^ (current char code)
            sum +=(index + len(key))**ord(c)
            # Perform modulus to keep hashsum in range [0, self.capacity - 1]
            sum = sum % self.capacity
        return sum
    
    def insert(self, key, value):
        # increase size 
        self.size += 1
        # get hash of the key
        hashKey = self.hash(key) # self, as we are accessing variable/method within the same class

        #get the node/bucket for this hashed key
        bucket = self.buckets[hashKey]

        #condition for empty bucket
        if bucket is None:
            # create a node at that bucket 
            self.buckets[hashKey] = Node(key, value)
            return

        # else collision and add to end of linked list
        prev = bucket # set the bucket that we are dealing with to prev
        while prev is not None:
            # take the current node, iterate to the end of (that linked list)
            prev = bucket
            bucket = bucket.next
        
        #prev has the last, set its next to the new node
        prev.next = Node(key, value)

    def find(self, key):
        # get the hash of the key to find the bucket
        # and then go to the last node of the linked list
        hashedKey = self.hash(key)
        bucket = self.buckets[hashedKey] # found the bucket

        #traverse the linked list
        while bucket is not None and bucket.key != key:
            bucket = bucket.next

        if bucket is None:
            return
        else:
            return bucket.value



  


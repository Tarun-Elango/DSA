from linked_list import Node, LinkedList
from blossom_lib import flower_definitions

class Hashmap:
  def __init__(self,size):
    self.size = size
    self.array = [LinkedList() for i in range(size)]

  def hashCode(self,key):
    return sum(key.encode())

  def compress(self,hashCode):
    return hashCode % self.size

  def assign(self, key, value):
    arrayIndex = self.compress(self.hashCode(key))
    payload = Node([key,value])
    list_at_array = self.array[arrayIndex]

    for i in list_at_array: # check the linked list at the position for key
      if key ==i[0]:
        i[1] = value
        return
    list_at_array.insert(payload) # add to the linked list
    # at the array position, if key not found
      

  def retreive(self, key):
    arrayIndex = self.compress( self.hashCode(key))
    list_at_array = self.array[arrayIndex]
    for i in list_at_array: # check the linked list at the
      if key == i[0]:
        return i[1]
    return None


blossom = Hashmap(len(flower_definitions))
for flowers in flower_definitions:
  blossom.assign(flowers[0], flowers[1]) 

print(blossom.retreive('daisy'))

'''
we are going to implement a 
hash map to relate the names 
of flowers to their meanings. 
In order to avoid collisions when
our hashing function collides the names 
of two flowers, we are going to use separate chaining.
'''
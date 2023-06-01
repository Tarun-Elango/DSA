# fifo
# operation add, remove, check (front/rear)

#using a list

queue =[]
queue_size = 100

def enqueue(value):
    if len(queue)==queue_size:
        print("queue full")

    queue.append(value)
    print(value,' added')

def dequeue():
    if len(queue)==0:
        print("queue empty")
    
    x= queue.pop(0)
    print('value removed -', x)

enqueue(100)
enqueue(200)
enqueue(300)
print('before')
print(queue)
print('after')
dequeue()
print(queue)
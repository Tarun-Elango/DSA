# lifo
# operation add, remove, check (front/rear)

#using a list

stack =[]
stack_size = 100

def enterToStack(value):
    if len(stack)==stack_size:
        print("queue full")

    stack.append(value)
    print(value,' added')

def removeFromStack():
    if len(stack)==0:
        print("queue empty")
    
    length= len(stack)-1
    x= stack.pop(length)
    print('value removed -', x)

enterToStack(100)
enterToStack(200)
enterToStack(300)
print('before')
print(stack)
print('after')
removeFromStack()
print(stack)
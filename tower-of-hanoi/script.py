from stack import Stack

print("\nLet's play Towers of Hanoi!!")

#Create the Stacks
stacks = []
left_stack = Stack("Left Stack")
middle_stack = Stack("Middle Stack")
right_stack = Stack("Right Stack")
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

#Set up the Game
# add the disks to the left stack

nums_of_disk = int(input("\nHow many disks do you want to play with?\n"))
num_disk = nums_of_disk
while(nums_of_disk < 3):
  print('enter number > 3')
  nums_of_disk = int(input("\nHow many disks do you want to play with?\n"))

# add disks to stack
while(nums_of_disk >0):
  left_stack.push(nums_of_disk)
  nums_of_disk-=1

number_optimal_moves = (2 ** nums_of_disk )- 1
print(f'fastest way is {number_optimal_moves}')
#Get User Input

def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while(True):
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print("enter {0} for {1}".format(letter, name))
    user_input  = str(input(''))

    if (user_input in choices):
      for i in range(len(stacks)):
        return stacks[i]
    print('choices is move ')


        
#Play the Game
num_user_moves = 0
# game ends when right stack is full
while right_stack.get_size() != num_disk :
  print("\n\n\n...Current Stacks...")
  for stack in stacks:
    print(stack.print_items())
  while(True):
    print("\nWhich stack do you want to move from?\n")
    from_stack = get_input()
    
    print("\nWhich stack do you want to move to?\n")
    to_stack= get_input() 
    if(from_stack.get_size()==0):
      print("\n\nInvalid Move. Try Again")
    elif to_stack.get_size()==0 or from_stack.peek()<to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break
    else: # move from large to small
      print("\n\nInvalid Move. Try Again")
      
print("\n\nYou completed the game in {0} moves, and the optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))


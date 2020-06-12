class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def set_next_node(self, next_node):
        self.next_node = next_node

    def get_next_node(self):
        return self.next_node

    def get_value(self):
        return self.value


class Stack:
    def __init__(self, name):
        self.size = 0
        self.top_item = None
        self.limit = 1000
        self.name = name

    def push(self, value):
        if self.has_space():
            item = Node(value)
            item.set_next_node(self.top_item)
            self.top_item = item
            self.size += 1
        else:
            print("No more room!")

    def pop(self):
        if self.size > 0:
            item_to_remove = self.top_item
            self.top_item = item_to_remove.get_next_node()
            self.size -= 1
            return item_to_remove.get_value()
        print("This stack is totally empty.")

    def peek(self):
        if self.size > 0:
            return self.top_item.get_value()
        print("Nothing to see here!")

    def has_space(self):
        return self.limit > self.size

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name

    def print_items(self):
        pointer = self.top_item
        print_list = []
        while (pointer):
            print_list.append(pointer.get_value())
            pointer = pointer.get_next_node()
        print_list.reverse()
        print("{0} Stack: {1}".format(self.get_name(), print_list))

if __name__ == '__main__':

# Create the Stacks

    left_stack = Stack("Left")
    middle_stack = Stack("Middle")
    right_stack = Stack("Right")
    stacks = [left_stack,middle_stack,right_stack]
# Set up the Game

# while num_disks<=3:
#     num_disks = int(input("\nHow many disks do you want to play with?\n"))
#     if num_disks <= 3:
#         print("Enter a number greater than or equal to 3\n")
    num_disks = 3
    for i in range(num_disks, 0, -1):
        left_stack.push(i)

    num_optimal_moves = 2 ** num_disks - 1
    print("The fastest you can solve this game is in {} moves".format(num_optimal_moves))

# Get User Input

    def get_input():
        choices = []
        for item in stacks:
            choices.append(item.get_name()[0])
        hello = True
        while hello:
            for i in range(len(stacks)):
                name = stacks[i].get_name()
                letter = choices[i]
                print("Enter {0} for {1}".format(letter, name))
            user_input = (raw_input("Enter selection")).upper()

            for i in range(len(stacks)):
                if user_input == choices[i]:
                    hello = False
                    break

        return stacks[i]

# Play the Game
    num_user_moves = 0
    while(right_stack.get_size() != num_disks):
        print("\n\n\n...Current Stacks...")
        for item in stacks:
            print(item.print_items())
        while True:
            print("\nWhich stack do you want to move from?\n")
            from_stack = get_input()
            print  ("\nWhich stack do you want to move to?\n")
            to_stack = get_input()
            if from_stack.is_empty():
                print("\n\nInvalid Move. Try Again")
            elif to_stack.is_empty() or (from_stack.peek()<to_stack.peek()):
                disk = from_stack.pop()
                to_stack.push(disk)
                num_user_moves+=1
                break
            else:
                print("\n\nInvalid Move. Try Again")

    print("\n\nYou completed the game in {0} moves, and the "
          "optimal number of moves is {1}".format(num_user_moves, num_optimal_moves))















# # Defining an empty pizza stack
# pizza_stack = Stack(6)
# # Adding pizzas as they are ready until we have
# pizza_stack.push("pizza #1")
# pizza_stack.push("pizza #2")
# pizza_stack.push("pizza #3")
# pizza_stack.push("pizza #4")
# pizza_stack.push("pizza #5")
# pizza_stack.push("pizza #6")
#
# # Uncomment the push() statement below:
# pizza_stack.push("pizza #7")
#
# # Delivering pizzas from the top of the stack down
# print("The first pizza to deliver is " + pizza_stack.peek())
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
# pizza_stack.pop()
#
# # Uncomment the pop() statement below:
# pizza_stack.pop()
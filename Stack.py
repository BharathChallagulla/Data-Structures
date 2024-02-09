class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def push(self, value):
        new_node = Node(value)

        new_node.next = self.top
        self.top = new_node
        self.height += 1
    
    def pop(self):
        if self.top is None:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp
    
    def print_stack(self):
        temp = self.top

        while temp:
            print(temp.value)
            temp = temp.next
    
# my_stack = Stack(9)

# my_stack.push(10)
# my_stack.push(11)
# print("before pop")
# my_stack.print_stack()

# my_stack.pop()

# print("after pop")
# my_stack.print_stack()

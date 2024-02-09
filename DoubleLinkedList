class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoubleLinkedList:
    
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.head is None:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop_first(self):
        if self.head is None:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        # if (index < 0) or (index >= self.length):
        #     return None
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next
        # return temp.value
        # below one optimised if we are tracking length
        if (index < 0) or (index >= self.length):
            return None
        temp = self.head
        if index < self.length//2:
            for _ in range(index):
                temp = temp.next
            return temp
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
            return temp
    
    def set(self, index, value):
        temp = self.get(index)
        if temp is None:
            return False
        temp.value = value
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)   
        if index == self.length:
            return  self.append(value)
        before = self.get(index-1)
        new_node = Node(value)
        after = before.next

        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        

        temp = self.get(index)

        temp.prev.next = temp.next
        temp.next.prev = temp.prev

        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp
    
    def reverse(self):
        if self.head is None:
            return None

        temp = self.head
        
        while temp:
            temp.prev, temp.next = temp.prev, temp.next
            temp = temp.prev
        self.head, self.tail = self.tail, self.head
    
    def swap_pairs(self):
        if self.head is None or self.head.next is None:
            return
        temp = self.head
        while temp and temp.next:
            temp.value, temp.next.value = temp.next.value, temp.value
            temp = temp.next.next
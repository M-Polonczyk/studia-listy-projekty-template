from random import randint

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self, list_size = 40):
        self.head = None
        for i in range(list_size):
            node = randint(65,67)
            if node == 65:
                dif = randint(1,4)
            if node == 66:
                dif = randint(5,8)
            if node == 67:
                dif = randint(9,12)
            self.add_node([chr(node), dif, i])
        
    def get_node(self, index):
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.data
            count += 1
            current = current.next
        return None

    def delete_node(self, index):
        if self.head is None:
            return
        
        if index == 0:
            self.head = self.head.next
            return
        
        current = self.head
        count = 0
        while current is not None and count < index - 1:
            current = current.next
            count += 1
            
        if current is None or current.next is None:
            return
        
        current.next = current.next.next

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            
    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

    def is_empty(self):
        return self.head is None or self.head == self.head.next
    
    def list_size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
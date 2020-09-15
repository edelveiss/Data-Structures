class Node:
    def __init__(self, value = None, next_node = None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return f"Value = {self.value}"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None 
        self.tail = None

    def __str__(self):
        output = ""
        if self.head is None:
            return "There are no any nodes"
        current_node = self.head

        while current_node:
            output += f"\n{current_node.get_value()}"
            current_node = current_node.get_next()
        return output

    def add_to_head(self, value): #O(1)
        new_node = Node(value) #create a new node to add
        #check if linked list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            #new_node should ppoint ot cuttent head
            new_node.next_node = self.head
            #move head to new node
            self.head = new_node 

    def add_to_tail(self, value):
        new_node = Node(value)
        if not self.head :
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            # self.tail.next_node = new_node
            self.tail = new_node

    def remove_head(self):
        if not self.head:
            return None
        head_value = self.head.get_value()
        if self.head.get_next() is None:
            self.head = None
            self.tail = None
            return head_value

        
        self.head = self.head.get_next()
        return head_value

    def remove_tail(self):
        if not self.head:
            return None

        if self.head is self.tail:
            head_value = self.head.get_value()
            self.head = None 
            self.tail = None
            return head_value

        current_node = self.head
        while current_node.get_next() is not self.tail:
            current_node = current_node.get_next()

        tail_value = self.tail.get_value()
        self.tail = current_node
        return tail_value

        

    # traversing    
    def contains(self, value):
        if self.head is None:
            return False

        #Loop throufh each node, until we see the value, or we cannot go futher
        current_node = self.head

        while current_node:
            #check if this is the node we are looking for
            if current_node.get_value() == value:
                return True
            #otherwise, go to the nest node
            current_node = current_node.get_next()
            # current_node = current_node.next_node
        return False

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current_node = self.head.get_next()
        while current_node:
            if current_node.get_value() > max_value:
                max_value = current_node.get_value()
            current_node = current_node.get_next()
        return max_value

            
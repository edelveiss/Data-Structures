from singly_linked_list import LinkedList
#------------------the linked list as the underlying storage-------------------------
#Stack class using the linked list as the underlying storage structure.
class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __str__(self):
        return self.storage.__str__()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size +=1
        return self.storage.add_to_tail(value)
        

    def pop(self):
        if self.size != 0:
            self.size -=1
            return self.storage.remove_tail()
        else:
            return None



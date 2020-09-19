from singly_linked_list import LinkedList
#-----------------linked list-----------------------------
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __str__(self):
        return self.storage.__str__()

    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return None

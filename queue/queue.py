"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
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

#-----------------list----------------------------------
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def get_storage(self):
#         return self.storage
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.size += 1
#         return self.storage.append(value)

#     def dequeue(self):
#         if self.storage.__len__() != 0:
#             self.size -= 1
#             removed_item = self.storage[0]
#             self.storage.remove(self.storage[0])
#             return removed_item
#         else:
#             return None

queue_var = Queue()
queue_var.enqueue(100)
queue_var.enqueue(101)
queue_var.enqueue(105)

print(queue_var, "length = ",queue_var.__len__())
queue_var.dequeue()
print(queue_var, "length = ",queue_var.__len__())
queue_var.dequeue()
print(queue_var, "length = ",queue_var.__len__())
queue_var.dequeue()
print(queue_var, "length = ",queue_var.__len__())


# queue_var.dequeue()
# print(queue_var.get_storage(), queue_var.__len__())
# queue_var.dequeue()
# print(queue_var.get_storage(), queue_var.__len__())
# queue_var.dequeue()
# print(queue_var.get_storage(), queue_var.__len__())
# queue_var.dequeue()
# print(queue_var.get_storage(), queue_var.__len__())
        

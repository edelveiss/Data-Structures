"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
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







#------------------array as the underlying storage-------------------------
#Stack class using an array as the underlying storage structure.
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def get_storage(self):
#         return self.storage

#     def __len__(self):
#         return self.size

#     def push(self, value):
#         self.size +=1
#         return self.storage.append(value)
        

#     def pop(self):
#         if self.size != 0:
#             self.size -=1
#             return self.storage.pop()
#         else:
#             return None

        
        

# stack_var = Stack()
# stack_var.push(100)
# stack_var.push(101)
# stack_var.push(105)
# print(stack_var.get_storage())
# print(stack_var.__len__())

# stack_var.pop()
# print(stack_var.__len__())
# print(stack_var.get_storage())
# stack_var.pop()
# print(stack_var.__len__())
# print(stack_var.get_storage())
# stack_var.pop()
# print(stack_var.__len__())
# print(stack_var.get_storage())



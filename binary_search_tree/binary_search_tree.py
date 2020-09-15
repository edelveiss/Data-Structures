"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from stack import Stack
from queue import Queue
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if self.value > value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

            
       

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)





    # Return the maximum value found in the tree
    def get_max(self):
        if self is None:
            return None
        while self.right:
            self = self.right
        return self.value

    def get_max_recursive(self):
        if self.right is None:
            return self.value
        return self.right.get_max_recursive()

    # Return the minimum value found in the tree
    def get_min(self):
        if self is None:
           return None
        while self.left:
            self = self.left
        return self.value
        
    def get_min_recursive(self):
        if self.left is None:
            return self.value
        return self.left.get_min_recursive()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        node_queue = Queue()
        node_queue.enqueue(self)

        while len(node_queue) > 0:
            current_node = node_queue.dequeue()
            print(current_node.value)

            if current_node.left:
                node_queue.enqueue(current_node.left)

            if current_node.right:
                node_queue.enqueue(current_node.right)

    # def bft_print(self):
    #     node_queue = []
    #     node_queue.append(self)
    #     while node_queue != []:
    #         current_node = node_queue.pop(0)
    #         print(current_node.value)
    #         if current_node.left:
    #             node_queue.append(current_node.left)
    #         if current_node.right:
    #             node_queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        node_stack = Stack()
        node_stack.push(self)
        while len(node_stack) > 0:
            current_node = node_stack.pop()
            print(current_node.value)

            if current_node.right:
                node_stack.push(current_node.right)

            if current_node.left:
                node_stack.push(current_node.left)

    # def dft_print(self):
    #     node_stack = []
    #     node_stack.append(self)
    #     while node_stack != []:
    #         current_node = node_stack.pop()
    #         print(current_node.value)
    #         if current_node.right:
    #             node_stack.append(current_node.right)
    #         if current_node.left:
    #             node_stack.append(current_node.left)
                

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
       
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)
        

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst1 = BSTNode(8)
bst1.insert(3)
bst1.insert(4)
bst1.insert(2)
bst1.insert(10)
bst1.insert(9)
bst1.insert(12)
print_node = lambda x: print(f'current value: {x}')
print(f"{'-'*20} for_each(){'-'*20}")
bst.for_each(print_node)
print(f"{'-'*20} in_order_print(){'-'*20}")
bst.in_order_print()
print(f"{'-'*20} get_max_recursive(){'-'*20}")
print(f'max is: {bst.get_max_recursive()}')
print(f"{'-'*20} get_min_recursive(){'-'*20}")
print(f'min is: {bst.get_min_recursive()}')
print(f"{'-'*20} bft_print(){'-'*20}")
bst1.bft_print()
print(f"{'-'*20} dft_print(){'-'*20}")
bst1.dft_print()

print("elegant methods")
print(f"{'-'*20} pre order(){'-'*20}")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()  

#-------------------------
print('*'*60)
print(f"{'-'*20} pre order(){'-'*20}")
print("pre order")
bst1.pre_order_dft()
print("in order")
bst1.in_order_print()
print("post order")
bst1.post_order_dft()  


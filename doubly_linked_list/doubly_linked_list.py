"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def __str__(self):
        return f"Value = {self.value}"

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev

    def set_prev(self, new_prev):
        self.prev = new_prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __str__(self):
        output = ""
        if self.head is None:
            return "There are no any nodes"
        current_node = self.head

        while current_node:
            output += f"\n{current_node.get_value()}"
            current_node = current_node.get_next()
        return output

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length +=1
        #check if linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #new_node should point ot current head
            new_node.set_next(self.head)
            self.head.set_prev(new_node)
            #move head to new node
            self.head = new_node 
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            return None
        # self.length -=1
        head_value = self.head.get_value()
        # if self.head.get_next() is None:
        #     self.head = None
        #     self.tail = None
        #     return head_value

        # self.head = self.head.get_next()
        # self.head.set_prev(None) 
        self.delete(self.head)
        return head_value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length +=1
        if not self.head :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_prev(self.tail)
            self.tail.set_next(new_node)
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.head:
            return None
        # self.length -=1
        tail_value = self.tail.get_value()
        # if self.head is self.tail:
        #     self.head = None 
        #     self.tail = None
        #     return tail_value
            

        # self.tail = self.tail.get_prev()
        # self.tail.set_next(None)
        self.delete(self.tail)
        return tail_value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if node is None or self.head is None or self.head is node:
            return 
        node_value = node.get_value()
        # if node is self.tail:
        #     self.remove_from_tail()
            
        # else:
        #     if node.get_prev():
        #         node.prev.set_next(node.get_next())
        #     if node.get_next():
        #         node.next.set_prev(node.get_prev())
        #     self.length -=1
        self.delete(node)
        self.add_to_head(node_value)


        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node is None or self.head is None or self.tail is node:
            return 
        node_value = node.get_value()
        # if node is self.head:
        #     self.remove_from_head()
            
        # else:
        #     if node.get_prev():
        #         node.prev.set_next(node.get_next())
        #     if node.get_next():
        #         node.next.set_prev(node.get_prev())
        #     self.length -=1
        self.delete(node)
        self.add_to_tail(node_value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if node is None or self.head is None:
            return
        self.length -= 1
        if self.head is self.tail and node is self.head:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = self.head.get_next()
            self.head.set_prev(None) 
        elif node == self.tail:
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)

        else:
            node.delete()
            # node.prev.set_next(node.get_next())
            # node.next.set_prev(node.get_prev())


           
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.get_value()
        current_node = self.head.get_next()
        while current_node:
            if max_value < current_node.get_value():
                max_value = current_node.get_value()
            current_node = current_node.get_next()
        return max_value
        
        

doubly_linked_list = DoublyLinkedList()
doubly_linked_list.add_to_head(1)
print("length = ", doubly_linked_list.length)
doubly_linked_list.add_to_head(2)
doubly_linked_list.add_to_head(3)
doubly_linked_list.remove_from_head()
doubly_linked_list.remove_from_head()
doubly_linked_list.remove_from_head()
print(doubly_linked_list)



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        if values:
            for value in values:
                self.insert_at_end(value)

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_by_value(self, value):
        if not self.head:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        curr = self.head
        while curr.next and curr.next.data != value:
            curr = curr.next
        if curr.next:
            curr.next = curr.next.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=" → ")
            curr = curr.next
        print("None")

    def traverse(self):
        """Traverse the list and return all data as a list."""
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        return elements

# --- Using the LinkedList ---

predefined_values = [2, 3, 4, 5, 6]
sll = LinkedList(predefined_values)

# Insert elements
sll.insert_at_end(10)
sll.insert_at_end(20)
sll.insert_at_beginning(5)
sll.insert_at_end(30)

# Display list
print("Singly Linked List:")
sll.display()

# Traverse the list and show contents as list
print("Traversed list data:", sll.traverse())  # New usage

# Delete an element
sll.delete_by_value(5)
print("After deleting 5:")
sll.display()

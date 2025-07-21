class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"(LinkedList) Pushed: {data}")

    def pop(self):
        if self.top is None:
            print("(LinkedList) Stack is empty!")
            return None
        popped = self.top.data
        self.top = self.top.next
        print(f"(LinkedList) Popped: {popped}")
        return popped

    def peek(self):
        if self.top is None:
            print("(LinkedList) Stack is empty!")
            return None
        print(f"(LinkedList) Top element: {self.top.data}")
        return self.top.data

    def update(self, old_value, new_value):
        current = self.top
        while current:
            if current.data == old_value:
                current.data = new_value
                print(f"(LinkedList) Updated {old_value} to {new_value}")
                return
            current = current.next
        print(f"(LinkedList) Value {old_value} not found!")

    def traverse(self):
        current = self.top
        print("(LinkedList) Stack contents (top to bottom):")
        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":
    print("=== Stack Using Linked List ===")
    ll_stack = StackLinkedList()
    ll_stack.push(10)
    ll_stack.push(20)
    ll_stack.push(30)
    ll_stack.traverse()
    ll_stack.peek()
    ll_stack.update(20, 25)
    ll_stack.pop()
    ll_stack.traverse()
    ll_stack.peek()
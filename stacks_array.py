class StackArray:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        print(f"(Array) Pushed: {data}")

    def pop(self):
        if not self.stack:
            print("(Array) Stack is empty!")
            return None
        popped = self.stack.pop()
        print(f"(Array) Popped: {popped}")
        return popped

    def peek(self):
        if not self.stack:
            print("(Array) Stack is empty!")
            return None
        print(f"(Array) Top element: {self.stack[-1]}")
        return self.stack[-1]

    def update(self, old_value, new_value):
        try:
            index = len(self.stack) - 1 - self.stack[::-1].index(old_value)
            self.stack[index] = new_value
            print(f"(Array) Updated {old_value} to {new_value}")
        except ValueError:
            print(f"(Array) Value {old_value} not found!")

    def traverse(self):
        print("(Array) Stack contents (top to bottom):")
        for item in reversed(self.stack):
            print(item)

if __name__ == "__main__":
    print("\n=== Stack Using Array ===")
    arr_stack = StackArray()
    arr_stack.push(100)
    arr_stack.push(200)
    arr_stack.push(300)
    arr_stack.traverse()
    arr_stack.peek()
    arr_stack.update(200, 250)
    arr_stack.pop()
    arr_stack.traverse()
    arr_stack.peek()
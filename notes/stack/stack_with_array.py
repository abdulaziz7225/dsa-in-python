# Stack implementation using an array
class Solution:
    # Constructor to initialize stack
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.stack = [0] * capacity
        self.index = -1

    # Push operation
    def push(self, value: int) -> None:
        if self.index == self.capacity - 1:
            print(f"Stack overflow. Cannot push {value}")
            return
        self.index += 1
        self.stack[self.index] = value
        print(f"{value} pushed to stack")

    # Pop operation
    def pop(self) -> int:
        if self.is_empty():
            print("Stack underflow. No elements to pop.")
            return -1
        top_element = self.stack[self.index]
        self.index -= 1
        return top_element

    # Peek / top operation
    def peek(self) -> int:
        if self.is_empty():
            print("Stack is empty")
            return -1
        return self.stack[self.index]

    def is_empty(self) -> bool:
        return self.index == -1

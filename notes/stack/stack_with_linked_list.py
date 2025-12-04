# Stack implementation using a linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    # Constructor to initialize stack
    def __init__(self) -> None:
        self.top = None

    # Push operation
    def push(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        print(f"{value} pushed to stack")

    # Pop operation
    def pop(self) -> int:
        if self.is_empty():
            print("Stack underflow. No elements to pop.")
            return -1
        top_element = self.top.value
        self.top = self.top.next
        return top_element

    # Peek / top operation
    def peek(self) -> int:
        if self.is_empty():
            print("Stack is empty")
            return -1
        return self.top.value

    def is_empty(self) -> bool:
        return self.top is None

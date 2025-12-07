class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, value: int):
        new_node = Node(value)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            return None

        temp = self.front
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.size -= 1
        return temp.value

    def peek(self):
        if self.front is None:
            return None
        return self.front.value

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size

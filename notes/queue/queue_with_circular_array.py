class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, element):
        if self.front == (self.rear + 1) % self.size:
            print("Queue is full")
            return None

        if self.front == -1:
            self.front = self.rear = 0
        elif self.rear == self.size - 1 and self.front != 0:
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty")
            return None

        data = self.queue[self.front]
        self.queue[self.front] = None
        if self.front == self.rear:
            self.front = self.rear = -1
        elif self.front == self.size - 1:
            self.front = 0
        else:
            self.front += 1
        return data

    def display_queue(self):
        if self.front == -1:
            print("Queue is empty")
            return None

        print("Elements in circular queue :")
        if self.rear >= self.front:
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
        print()

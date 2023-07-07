class Node:
    def __init__(self, data):
        # Constructor to initialize a node
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        # Constructor to initialize the queue
        self.front = None
        self.rear = None

    def is_empty(self):
        # Check if the queue is empty
        return self.front is None

    def enqueue(self, data):
        # Enqueue an element into the queue
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        # Dequeue the front element from the queue
        if self.is_empty():
            return None

        dequeued_data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next

        return dequeued_data

    def peek(self):
        # Peek the front element of the queue without removing it
        if self.is_empty():
            return None
        return self.front.data



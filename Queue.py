class DynamicQueue:
    def __init__(self):
        self.queue = []  # Initialize an empty array
        self.front = 0  # Points to the front of the queue
        self.rear = -1  # Points to the rear of the queue (index of the last element)

    def enqueue(self, value):
        """Adds an element to the rear of the queue."""
        self.queue.append(value)
        self.rear += 1  # Move the rear pointer to the new last element

    def dequeue(self):
        """Removes an element from the front of the queue."""
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")

        value = self.queue[self.front]
        self.front += 1  # Move the front pointer to the next element

        # Trim unused space in the array when it grows too large
        if self.front > len(self.queue) // 2:
            self.queue = self.queue[self.front:]
            self.rear -= self.front
            self.front = 0

        return value

    def peek(self):
        """Returns the element at the front without removing it."""
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[self.front]

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front > self.rear

    def size(self):
        """Returns the number of elements in the queue."""
        return self.rear - self.front + 1


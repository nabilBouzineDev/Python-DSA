class Queue:
    def __init__(self, capacity):
        self.front = self.size = 0
        self.rear = capacity - 1
        # F.E: if a queue had capacity 5 -> This Q will create an array with 5 (None) elements
        self.Q = [None] * capacity
        self.capacity = capacity

    def is_full(self):
        return self.size == self.capacity

    def is_empty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.is_full():
            print("Full")
            return

        self.rear = (self.rear + 1) % self.capacity
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("%s enqueued to Queue" % str(item))

    def dequeue(self):
        if self.is_empty():
            print("Empty")
            return

        print("%s dequeued from Queue" % str(self.Q[self.front]))
        self.front = (self.front + 1) % self.capacity
        self.size = self.size - 1

    def queue_front(self):
        if self.is_empty():
            print("Empty")
            return

        print("Font item is", self.Q[self.front])

    def queue_rear(self):
        if self.is_empty():
            print("Empty")
            return

        print("Rear item is", self.Q[self.rear])

    def print(self):
        print("Size of the Queue is", self.size)
        print("="*5)
        for index in range(self.front, self.rear):
            print(self.Q[index])
        print("="*5)


if __name__ == '__main__':
    queue = Queue(30)
    queue.print()
    print()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.print()
    queue.queue_front()
    queue.queue_rear()
    print()
    queue.dequeue()
    queue.print()
    queue.queue_front()
    queue.queue_rear()
    print()


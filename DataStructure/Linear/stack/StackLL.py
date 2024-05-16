from DataStructure.Linear.LinkedList import Node


class Stack:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def print_stack(self):
        if self.is_empty():
            print("Oops! nothing to print here; stack is empty!")
            return

        print("=" * 5)
        current = self.root
        while current:
            print(current.data)
            current = current.next
        print("=" * 5)

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node
        print("%d pushed to stack" % data)

    def pop(self):
        if self.is_empty():
            return float("-inf")

        popped = self.root.data
        self.root = self.root.next
        print("%d popped from stack" % popped)
        return popped

    def peek(self):
        if self.is_empty():
            return float("-inf")
        print("Top element is %d" % self.root.data)
        return self.root.data


if __name__ == '__main__':
    stack = Stack()

    stack.print_stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.peek()

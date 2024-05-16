class Stack:
    def __init__(self):
        self.my_stack = []

    def is_empty(self):
        return len(self.my_stack) == 0

    def print_stack(self):
        if self.is_empty():
            print("Oops! nothing to print here; stack is empty!")
            return

        print("=" * 5)
        for element in range(len(self.my_stack) - 1, -1, -1):
            print(self.my_stack[element])
        print("=" * 5)

    def push(self, new_element):
        self.my_stack.append(new_element)
        print(f'{new_element} pushed to the stack!')

    def pop(self):
        if self.is_empty():
            print("Oops! stack is empty")
            return

        print(f'{self.my_stack[-1]} popped from the stack!')
        return self.my_stack.pop()

    def peek(self):
        if self.is_empty():
            print("Oops! stack is empty")
            return
        print(f'Top element is {self.my_stack[-1]}')


if __name__ == '__main__':
    stack = Stack()
    stack.print_stack()
    stack.pop()
    stack.peek()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    stack.pop()
    stack.print_stack()
    stack.peek()

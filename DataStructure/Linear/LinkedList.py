class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # move to the last element or the given element
    def _walk_to(self, target=None):
        if target is None:
            current = self.head
            while current.next:
                current = current.next
            return current
        else:
            current = self.head
            while current.next.data is not target.data:
                current = current.next
            return current

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # ex: llist = A -> B -> C and we want to add Node N at the first
    def push(self, data):
        new_node = Node(data)  # N created
        new_node.next = self.head  # N -> A* -> B -> C  (* is the head)
        self.head = new_node  # N* -> A -> B -> C

    # Add new node after previous node
    def insert_after(self, prev_node, data):

        if prev_node is None:
            print("Oops, we can't find this node in the llist")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Add new node at the last
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self._walk_to()
        last.next = new_node

    def delete_node(self, target_data):
        if target_data == self.head.data:
            self.head = self.head.next
            return

        older_node = Node(target_data)
        prev_node = self._walk_to(older_node)
        prev_node.next = prev_node.next.next


if __name__ == '__main__':
    # Starting with empty list
    lList = LinkedList()

    lList.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)

    # Linking these nodes
    lList.head.next = second  # link head node with second node
    second.next = third  # link second node with third node
    third.next = fourth

    lList.insert_after(third, 8)
    lList.print_list()
    print("*"*20)
    lList.delete_node(4)
    lList.print_list()

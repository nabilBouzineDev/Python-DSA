class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# We travel nodes in binary tree in order(L.N.R)!
def in_order(tree_root):
    # Check if the tree contains elements!
    if not tree_root:
        return

    in_order(tree_root.left)
    print(tree_root.data, end=" ")
    in_order(tree_root.right)


def insert(tree, data):
    # This list will store tree elements
    q = [tree]

    while len(q):
        tree = q[0]
        q.pop(0)

        if not tree.left:
            tree.left = Node(data)
            break
        else:
            q.append(tree.left)

        if not tree.right:
            tree.right = Node(data)
            break
        else:
            q.append(tree.right)


if __name__ == '__main__':
    root = Node(10)

    root.left = Node(11)
    root.left.left = Node(7)

    root.right = Node(9)
    root.right.left = Node(15)
    root.right.right = Node(8)

    in_order(root)
    print()
    insert(root, 12)
    in_order(root)

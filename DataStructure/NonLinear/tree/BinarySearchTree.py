class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order(tree_root):
    if tree_root:
        in_order(tree_root.left)
        print(tree_root.data, end="\n")
        in_order(tree_root.right)


def insert(tree_root, new_node):
    if tree_root is None:
        tree_root = new_node
    else:
        if new_node.data > tree_root.data:
            if tree_root.right is None:
                tree_root.right = new_node
            else:
                insert(tree_root.right, new_node)
        else:
            if tree_root.left is None:
                tree_root.left = new_node
            else:
                insert(tree_root.left, new_node)


def _search(tree_root, target_data):
    if tree_root is None or tree_root.data == target_data:
        return tree_root

    if tree_root.data < target_data:
        return _search(tree_root.right, target_data)

    return _search(tree_root.left, target_data)


def searcher(tree_root, value):
    temp = _search(tree_root, value)
    print("The number is not found") if temp is None else print("The number {} is found".format(temp.data))


def min_value_node(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


def delete_node(tree_root, target_node_data):
    # Base Case
    if tree_root is None:
        return tree_root

    # Search in the right subtree
    if target_node_data > tree_root.data:
        tree_root.right = delete_node(tree_root.right, target_node_data)

    # Search in left subtree
    elif target_node_data < tree_root.data:
        tree_root.left = delete_node(tree_root.left, target_node_data)

    # Current node is our target node to delete.
    else:

        # Case 1, 2: No child, one child
        if tree_root.left is None:
            return tree_root.right

        elif tree_root.right is None:
            return tree_root.left

        # Case 3: Two children
        # Get the smallest node in the right subtree
        temp = min_value_node(tree_root.right)

        # Assign it to the current root
        tree_root.data = temp.data

        # Delete the smallest node from the origin place
        tree_root.right = delete_node(tree_root.right, temp.data)

    return tree_root


if __name__ == '__main__':
    root = Node(50)

    insert(root, Node(30))
    insert(root, Node(20))
    insert(root, Node(40))
    insert(root, Node(70))
    insert(root, Node(60))
    insert(root, Node(80))

    in_order(root)
    print("*" * 10)
    searcher(root, 40)

    print("\nTree is modified after delete:")
    delete_node(root, 20)
    delete_node(root, 40)
    in_order(root)
    searcher(root, 40)

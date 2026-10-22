
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.data:
        root.left = insert(root.left, value)
    elif value > root.data:
        root.right = insert(root.right, value)
    else:
        print("Duplicate values not allowed!")

    return root


def search(root, value):
    if root is None or root.data == value:
        return root

    if value < root.data:
        return search(root.left, value)

    return search(root.right, value)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def minimum(root):
    if root is None:
        return None
    while root.left:
        root = root.left
    return root.data


def maximum(root):
    if root is None:
        return None
    while root.right:
        root = root.right
    return root.data


def delete(root, value):
    if root is None:
        return None

    if value < root.data:
        root.left = delete(root.left, value)

    elif value > root.data:
        root.right = delete(root.right, value)

    else:
        # Node has no left child
        if root.left is None:
            return root.right

        # Node has no right child
        if root.right is None:
            return root.left

        # Node has two children
        successor = root.right
        while successor.left:
            successor = successor.left

        root.data = successor.data
        root.right = delete(root.right, successor.data)

    return root


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def height(root):
    if root is None:
        return 0
    return 1 + max(height(root.left), height(root.right))


root = None

while True:
    print("\n===== BST USING LINKED NODES =====")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Find Minimum")
    print("8. Find Maximum")
    print("9. Count Nodes")
    print("10. Height")
    print("0. Exit")

    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = int(input("Enter value: "))
            root = insert(root, value)

        elif choice == 2:
            value = int(input("Enter value to search: "))
            if search(root, value):
                print("Element found!")
            else:
                print("Element not found!")

        elif choice == 3:
            value = int(input("Enter value to delete: "))
            if search(root, value):
                root = delete(root, value)
                print("Deleted successfully!")
            else:
                print("Element not found!")

        elif choice == 4:
            print("Inorder:", end=" ")
            inorder(root)
            print()

        elif choice == 5:
            print("Preorder:", end=" ")
            preorder(root)
            print()

        elif choice == 6:
            print("Postorder:", end=" ")
            postorder(root)
            print()

        elif choice == 7:
            print("Minimum =", minimum(root))

        elif choice == 8:
            print("Maximum =", maximum(root))

        elif choice == 9:
            print("Total nodes =", count_nodes(root))

        elif choice == 10:
            print("Height =", height(root))

        elif choice == 0:
            print("Program terminated.")
            break

        else:
            print("Invalid choice!")



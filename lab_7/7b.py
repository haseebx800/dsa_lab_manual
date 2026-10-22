
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def create_tree(self):
        self.root = Node('A')
        self.root.left = Node('B')
        self.root.right = Node('C')
        self.root.left.left = Node('D')
        self.root.left.right = Node('E')
        self.root.right.right = Node('F')
        print("Binary tree created successfully!")

    def preorder(self, node):
        if node is None:
            return
        print(node.data, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.left)
        print(node.data, end=" ")
        self.inorder(node.right)

    def postorder(self, node):
        if node is None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=" ")

    def level_order(self):
        if self.root is None:
            print("Tree is empty!")
            return

        queue = [self.root]

        while queue:
            node = queue.pop(0)
            print(node.data, end=" ")

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)


tree = BinaryTree()

while True:
    print("\n\n--- BINARY TREE USING LINKED NODES ---")
    print("1. Create Tree")
    print("2. Preorder Traversal")
    print("3. Inorder Traversal")
    print("4. Postorder Traversal")
    print("5. Level-order Traversal")
    print("0. Exit")

    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            tree.create_tree()

        elif choice == 2:
            if tree.root is None:
                print("Create the tree first!")
            else:
                print("Preorder: ", end="")
                tree.preorder(tree.root)
                print()

        elif choice == 3:
            if tree.root is None:
                print("Create the tree first!")
            else:
                print("Inorder: ", end="")
                tree.inorder(tree.root)
                print()

        elif choice == 4:
            if tree.root is None:
                print("Create the tree first!")
            else:
                print("Postorder: ", end="")
                tree.postorder(tree.root)
                print()

        elif choice == 5:
            print("Level-order: ", end="")
            tree.level_order()
            print()

        elif choice == 0:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")



class BinaryTreeArray:
    def __init__(self, size):
        self.tree = [None] * size
        self.size = size

    def set_root(self, data):
        self.tree[0] = data
        print("Root set successfully!")

    def set_left(self, parent_index, data):
        if parent_index < 0 or parent_index >= self.size:
            print("Invalid parent index!")
            return

        if self.tree[parent_index] is None:
            print("Parent node does not exist!")
            return

        child_index = 2 * parent_index + 1

        if child_index < self.size:
            self.tree[child_index] = data
            print("Left child set successfully!")
        else:
            print("Index out of range!")

    def set_right(self, parent_index, data):
        if parent_index < 0 or parent_index >= self.size:
            print("Invalid parent index!")
            return

        if self.tree[parent_index] is None:
            print("Parent node does not exist!")
            return

        child_index = 2 * parent_index + 2

        if child_index < self.size:
            self.tree[child_index] = data
            print("Right child set successfully!")
        else:
            print("Index out of range!")

    def preorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        print(self.tree[index], end=" ")
        self.preorder(2 * index + 1)
        self.preorder(2 * index + 2)

    def inorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        self.inorder(2 * index + 1)
        print(self.tree[index], end=" ")
        self.inorder(2 * index + 2)

    def postorder(self, index=0):
        if index >= self.size or self.tree[index] is None:
            return
        self.postorder(2 * index + 1)
        self.postorder(2 * index + 2)
        print(self.tree[index], end=" ")

    def level_order(self):
        for value in self.tree:
            if value is not None:
                print(value, end=" ")

    def display(self):
        print("\nArray Representation:")
        for i in range(self.size):
            print(f"Index {i}: {self.tree[i]}")


size = int(input("Enter the size of the tree: "))
tree = BinaryTreeArray(size)

while True:
    print("\n\n--- BINARY TREE USING ARRAY ---")
    print("1. Set Root")
    print("2. Set Left Child")
    print("3. Set Right Child")
    print("4. Preorder Traversal")
    print("5. Inorder Traversal")
    print("6. Postorder Traversal")
    print("7. Level-order Traversal")
    print("8. Display Array")
    print("0. Exit")

    while True:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = input("Enter root data: ")
            tree.set_root(data)

        elif choice == 2:
            parent = int(input("Enter parent index: "))
            data = input("Enter left child data: ")
            tree.set_left(parent, data)

        elif choice == 3:
            parent = int(input("Enter parent index: "))
            data = input("Enter right child data: ")
            tree.set_right(parent, data)

        elif choice == 4:
            print("Preorder: ", end="")
            tree.preorder()
            print()

        elif choice == 5:
            print("Inorder: ", end="")
            tree.inorder()
            print()

        elif choice == 6:
            print("Postorder: ", end="")
            tree.postorder()
            print()

        elif choice == 7:
            print("Level-order: ", end="")
            tree.level_order()
            print()

        elif choice == 8:
            tree.display()

        elif choice == 0:
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Try again.")



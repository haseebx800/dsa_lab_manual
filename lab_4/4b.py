class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next

                temp.next = new_node
                new_node.prev = temp

        print("Linked List created successfully")

    # 2. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

        print(f"Inserted {data} at the beginning.")

    # 3. Insert at End
    def insert_end(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            print(f"Inserted {data} at the end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

        print(f"Inserted {data} at the end.")

    # 4. Insert at Index
    def insert_at_index(self):
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            new_node = Node(data)
            new_node.next = self.head

            if self.head is not None:
                self.head.prev = new_node

            self.head = new_node
            return

        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Index out of range")
                return

            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        new_node = Node(data)

        new_node.next = temp.next
        new_node.prev = temp

        if temp.next is not None:
            temp.next.prev = new_node

        temp.next = new_node

        print(f"Inserted {data} at index {index}.")

    # 5. Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

        print("Deleted beginning node.")

    # 6. Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            print("Deleted last node.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

        print("Deleted last node.")

    # 7. Delete from Index
    def delete_at_index(self):
        index = int(input("Enter index: "))

        if self.head is None:
            print("List is empty")
            return

        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.head = self.head.next

            if self.head is not None:
                self.head.prev = None

            print("Deleted node value.")
            return

        temp = self.head

        for i in range(index):
            if temp is None:
                print("Index out of range")
                return

            temp = temp.next

        if temp is None:
            print("Index out of range")
            return

        if temp.next is not None:
            temp.next.prev = temp.prev

        if temp.prev is not None:
            temp.prev.next = temp.next

        print("Deleted node value.")

    # 8. Count Nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main Program
dll = DLL()

while True:
    print("\n----- DOUBLY LINKED LIST -----")
    print("1. Create Linked List")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete from Beginning")
    print("6. Delete from End")
    print("7. Delete from Index")
    print("8. Count number of nodes")
    print("9. Display")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.create()

    elif choice == 2:
        dll.insert_beginning()

    elif choice == 3:
        dll.insert_end()

    elif choice == 4:
        dll.insert_at_index()

    elif choice == 5:
        dll.delete_beginning()

    elif choice == 6:
        dll.delete_end()

    elif choice == 7:
        dll.delete_at_index()

    elif choice == 8:
        dll.count_nodes()

    elif choice == 9:
        dll.display()

    elif choice == 10:
        print("Exiting from the program...")
        break

    else:
        print("Invalid choice")

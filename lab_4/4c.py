class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CLL:
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
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                temp.next = new_node
                new_node.next = self.head

        print("Linked List created successfully")

    # 2. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print(f"Inserted {data} at the beginning.")
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        self.head = new_node
        temp.next = self.head

        print(f"Inserted {data} at the beginning.")

    # 3. Insert at End
    def insert_end(self):
        data = int(input("Enter data: "))

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            print(f"Inserted {data} at the end.")
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

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

            if self.head is None:
                self.head = new_node
                new_node.next = self.head
            else:
                temp = self.head

                while temp.next != self.head:
                    temp = temp.next

                new_node.next = self.head
                self.head = new_node
                temp.next = self.head

            print(f"Inserted {data} at index {index}.")
            return

        if self.head is None:
            print("Index out of range")
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Index out of range")
                return

        new_node = Node(data)

        new_node.next = temp.next
        temp.next = new_node

        print(f"Inserted {data} at index {index}.")

    # 5. Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            print("Deleted beginning node.")
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        self.head = self.head.next
        temp.next = self.head

        print("Deleted beginning node.")

    # 6. Delete from End
    def delete_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            print("Deleted last node.")
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head

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
            self.delete_beginning()
            return

        temp = self.head

        for i in range(index - 1):
            temp = temp.next

            if temp == self.head:
                print("Index out of range")
                return

        if temp.next == self.head:
            print("Index out of range")
            return

        temp.next = temp.next.next

        print("Deleted node value.")

    # 8. Count Nodes
    def count_nodes(self):
        if self.head is None:
            print("Number of nodes: 0")
            return

        count = 0
        temp = self.head

        while True:
            count += 1
            temp = temp.next

            if temp == self.head:
                break

        print("Number of nodes:", count)

    # 9. Display
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(HEAD)")


# Main Program
cll = CLL()

while True:
    print("\n----- CIRCULAR LINKED LIST -----")
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
        cll.create()

    elif choice == 2:
        cll.insert_beginning()

    elif choice == 3:
        cll.insert_end()

    elif choice == 4:
        cll.insert_at_index()

    elif choice == 5:
        cll.delete_beginning()

    elif choice == 6:
        cll.delete_end()

    elif choice == 7:
        cll.delete_at_index()

    elif choice == 8:
        cll.count_nodes()

    elif choice == 9:
        cll.display()

    elif choice == 10:
        print("Exiting from the program...")
        break

    else:
        print("Invalid choice")

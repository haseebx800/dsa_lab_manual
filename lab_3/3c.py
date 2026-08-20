def insertion_sort(a, n):
    for i in range(1, n):
        key = a[i]
        for j in range(i - 1, -1, -1):
            if a[j] > key:
                a[j + 1] = a[j]
            else:
                break
        a[j + 1] = key
    return a
n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)
print("Sorted array:", insertion_sort(a, n))

def selection_sort(a, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a
n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)
print("Sorted array:", selection_sort(a, n))

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[-1]
    left = []
    right = []
    for i in range(len(a) - 1):
        if a[i] <= pivot:
            left.append(a[i])
        else:
            right.append(a[i])
    return quick_sort(left) + [pivot] + quick_sort(right)
n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)
a = quick_sort(a)
print("Sorted array:", a)

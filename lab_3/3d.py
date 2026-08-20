def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) 
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = 0
    j = 0
    for k in range(len(left) + len(right)):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result
n = int(input("Enter number of elements: "))
a = []
for i in range(n):
    x = int(input("Enter element: "))
    a.append(x)
a = merge_sort(a)
print("Sorted array:", a)

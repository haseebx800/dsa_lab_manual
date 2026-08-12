def binary_search(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
arr=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
arr.sort()
x=int(input("Enter element to search: "))
result=binary_search(arr,x)
if result==-1:
    print("Element not found")
else:
    print("Element found at index",result)

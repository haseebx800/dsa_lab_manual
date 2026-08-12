def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1
arr=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    arr.append(int(input("Enter element: ")))
x=int(input("Enter element to search: "))
result=linear_search(arr,x)
if result==-1:
    print("Element not found")
else:
    print("Element found at index",result)

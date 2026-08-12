def search(arr,id,n):
    if n==len(arr):
        return -1
    if arr[n]==id:
        return n
    return search(arr,id,n+1)
arr=[101,102,103,104,105]
id=int(input("Enter employee ID: "))
result=search(arr,id,0)
if result==-1:
    print("Employee ID not found")
else:
    print("Employee ID found at index",result)

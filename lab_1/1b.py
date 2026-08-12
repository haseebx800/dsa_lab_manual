def power(p,n):
    if n==0:
        return 1
    return p*power(p,n-1)
p=int(input("Enter p: "))
n=int(input("Enter n: "))
print(power(p,n))

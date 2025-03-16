def rev(n):
    result=[]
    for i in range(n, 0, -1):
        result.append(i)
    return result

n=int(input("n:"))
k=rev(n)
print(k)
def reverse(str):
    a = str.split()
    reversed_a = a[::-1] 
    return " ".join(reversed_a)

str = str(input("text: "))
print ( reverse(str) )
    
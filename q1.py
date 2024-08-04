
def func1(a,b,c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
    else:
        print("noting")

a= int(input("Enter the value a:"))
b= int(input("Enter the value b:"))
c= int(input("Enter the value c:"))

print (func1(a,b,c))
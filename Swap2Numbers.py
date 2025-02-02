def swap(a,b):
    a=a^b
    b=a^b
    a=a^b

    print(f"After swapping, the value of a is {a} and the value of b is {b}")

def swap2(a,b):
    a=(a&b)+(a|b)
    b=(a+(~b)+1)
    a=(a+(~b)+1)

    print(f"After swapping, the value of a is {a} and the value of b is {b}")

n1=int(input("Enter a value for a: "))
n2=int(input("Enter a value for b: "))

swap(n1,n2)
swap2(n1,n2)
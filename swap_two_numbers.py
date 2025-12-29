def swap(a,b):
    return b,a
a,b = map(int,input("enter numbers").split())
a,b=swap(a,b)
print(a,b)
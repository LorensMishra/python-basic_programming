def even_or_odd(n):
    return "even" if (n%2 == 0) else "odd"
n = int(input("enter a number: "))
if n<0:
    print("Enter a positive number")
else:
    print(even_or_odd(n))
def reverse(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num %10
        num //= 10
    print("Reversed number:", rev)
num = int(input("enter a number: "))
reverse(num)
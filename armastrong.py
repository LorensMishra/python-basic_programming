def arm(n):
    temp = n
    digits = len(str(n))
    total = 0
    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10
    
    if temp == total:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")         
n = int(input("enter a number: "))  
arm(n) 
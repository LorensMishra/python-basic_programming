"""
Docstring for prime_no
def prime(num):
    if num > 0:
        for i in range(2, num+1):
            if num%i == 0:
                print("prime number", num)
            else:
                print("not a prime number")
n = int(input("enter a number"))
print(prime(n))

"""

"""
def is_prime_basic(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

"""

def is_prime_sqrt(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Take input from user
num = int(input("Enter a number: "))

# Check if number is prime
if is_prime_sqrt(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is NOT a prime number.")

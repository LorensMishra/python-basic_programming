def product_of_digit(n):
    prod = 0
    for i in range(1, n+1):
        prod = prod*10 + n%10
        n //=10
    return prod
n = int(input( ))
print(product_of_digit(n))
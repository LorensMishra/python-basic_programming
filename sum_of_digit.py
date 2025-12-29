def sum_of_digit(n):
    num = 0
    while n > 0:
        num += n%10
        n //= 10
    return num
n = int(input( ))
print(sum_of_digit(n))
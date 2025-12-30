def gcd_lcm(a,b):
    x,y =a,b
    while y != 0:
        x,y = y,x %y
    gcd = x
    lcm = (a*b) // gcd
    print("gcd", gcd)
    print("lcm", lcm)
a = int(input())
b = int(input()) 
gcd_lcm(a,b)          
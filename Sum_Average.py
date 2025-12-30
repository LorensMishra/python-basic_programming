def sum_avg(arr):
    total = 0
    for i in arr:
        total += i
    print(total)
    
    avg = total/len(arr)
    print(avg)


arr = list(map(int,input("enter a number ").split()))
sum_avg(arr)
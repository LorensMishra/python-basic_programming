"""
arr = list(map(int, input("enter a number seperated by space: ").split()))
maxnum = max(arr)
minnum = min(arr)
print(maxnum,minnum)

"""
def largest_smallest(arr):
    largest = arr[0]
    smallest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
            
        if i < smallest:
            smallest = i
    print("largest", largest)
    print("smallest", smallest)

arr = list(map(int, input("enter a number").split()))
largest_smallest(arr)
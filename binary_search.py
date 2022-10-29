
def bsearch(array, N, x):
    lower = 1
    upper = N
    while upper >= lower:
        mid = (lower+upper)//2
        if x == array[mid]:
            print("Success")
            return mid
        elif x < array[mid]:
            upper = mid - 1
        else:
            lower = mid + 1
    return -1


A = [1,4,6,9,11,32]

print(bsearch(A, len(A), 9))
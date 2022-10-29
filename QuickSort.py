lst = [7, 6, 2, 1, 5]


def partition(array, p, r):
    x = array[r]
    i = p-1
    
    for j in range(p, r):
        if array[j] <= x:
            i = i+1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[r] = array[r], array[i+1]
    return i+1


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


quicksort(lst, 0, len(lst)-1)

print(lst)
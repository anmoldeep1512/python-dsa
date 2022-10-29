def merge(array, lower, mid, upper):
    n1 = mid - lower + 1
    n2 = upper - mid
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = array[lower + i]
    for j in range(0, n2):
        R[j] = array[mid + j + 1]

    i = 0
    j = 0
    k = lower

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + (r - 1)) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


A = [82, 64, 22, 66, 1, 3, 98, 55]
mergeSort(A, 0, len(A)-1)
print(A)
import random


arr = [random.randint(0, 100) for _ in range(10)]


def mergeSort(left: int, right: int):
    if left >= right:
        return
    mid = (right - left) // 2 + left
    mergeSort(left, mid)
    mergeSort(mid + 1, right)
    merge(left, mid, right)


def merge(left: int, mid: int, right: int):
    n1 = mid - left + 1
    n2 = right - mid
    larr = [0] * n1
    rarr = [0] * n2

    for i in range(mid - left + 1):
        larr[i] = arr[left + i]
    for i in range(right - mid):
        rarr[i] = arr[mid + 1 + i]

    i, j, k = 0, 0, left
    while i < mid - left + 1 and j < right - mid:
        if larr[i] < rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1
    while i < mid - left + 1:
        arr[k] = larr[i]
        k += 1
        i += 1

    while j < right - mid:
        arr[k] = rarr[j]
        k += 1
        j += 1


print(arr)
mergeSort(0, len(arr) - 1)
print(arr)

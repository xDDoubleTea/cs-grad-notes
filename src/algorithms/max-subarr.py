import random


class SubArrRepr:
    def __init__(self, left: int, right: int, sum: int):
        self.left: int = left
        self.right: int = right
        self.sum: int = sum

    def __gt__(self, rhs):
        return self.sum > rhs.sum

    def __lt__(self, rhs):
        return self.sum < rhs.sum

    def __eq__(self, rhs):
        return self.sum == rhs.sum

    def __repr__(self) -> str:
        return f"{arr[self.left : self.right + 1]}, Sum = {self.sum}"


def divide_and_conquer(arr, left: int, right: int) -> SubArrRepr:
    if left > right:
        return SubArrRepr(left, right, -10000)
    if left == right:
        return SubArrRepr(left, right, arr[left])
    mid = (left + right) // 2
    larr = divide_and_conquer(arr, left, mid)
    rarr = divide_and_conquer(arr, mid + 1, right)

    rightSum = leftSum = -100000

    # go right from element at mid + 1
    sum = 0
    i = mid + 1
    maxRend = i
    while i <= right:
        sum += arr[i]
        if rightSum < sum:
            rightSum = sum
            maxRend = i
        i += 1

    # go left from mid element
    sum = 0
    i = mid
    maxLend = i
    while i >= left:
        sum += arr[i]
        if leftSum < sum:
            leftSum = sum
            maxLend = i
        i -= 1
    return max(larr, rarr, SubArrRepr(maxLend, maxRend, leftSum + rightSum))


def naive(arr) -> SubArrRepr:
    maxSum = -100000
    maxsubarr = SubArrRepr(0, 0, maxSum)
    for i in range(len(arr)):
        sum = 0
        l_end = r_end = i
        for j in range(i, len(arr)):
            sum += arr[j]
            if sum > maxSum:
                maxSum = sum
                r_end = j

        maxsubarr = max(maxsubarr, SubArrRepr(l_end, r_end, maxSum))

    return maxsubarr


# print("Maximum Subarray Sum")


for i in range(100000):
    arr = [random.randint(-100, 100) for _ in range(10)]
    print(arr)
    assert naive(arr) == divide_and_conquer(arr, 0, len(arr) - 1)

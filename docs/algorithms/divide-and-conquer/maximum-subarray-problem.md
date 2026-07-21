# The Maximum Subarray Problem

!!! problem "The Maximum Subarray Problem"

    Given an array with $n$ elements, find the subarray where its elements have the maximum sum.

!!! solution

    !!! solution "Divide and Conquer"

        - 將陣列對半切，得到$L,R$兩個陣列
        - 對$L,R$作遞迴，分別得到$L$跟$R$中的最大子陣列$L_{max}$跟$R_{max}$
        - 合併時不只比較左右兩邊，還要看有沒有橫跨兩邊且比左右兩邊都大的子列

        ???+ solution "Code"
            ```python
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
            ```

        !!! solution "Complexity"

            - **Time Complexity**

                對半切再合起來就是$T(n)=2T(n/2)+f(n)$，合併用的算法是線性所以$f(n)=O(n)$，長得跟mergesort一模一樣所以就是$O(n\log n)$

            - **Space Complexity**

                需要function call，function call裡面用到常數資源（`leftSum, rightSum, i, mid, sum, maxLend, maxRend`），function call不重疊，所以總共就是$O(\log n)$

    !!! solution "Dynamic programming"

        ???+ solution "Code"

"""
Binary Search Template II
Initial Condition: left = 0, right = len(array) - 1
Termination: left + 1 == right
Searching right: left = middle
Searching left: right = middle
"""

from typing import List


class Solution:
    def binary_search(self, array: List[int], target: int) -> int:
        left = 0
        right = len(array) - 1

        while left + 1 < right:
            middle = (left + right) // 2

            # Find ANY index of the target
            # if array[middle] == target:
                # return middle
            if array[middle] < target:
                left = middle
            else:
                right = middle

        # Post-processing
        # End Condition: left + 1 == right
        if array[left] == target:
            return left
        if array[right] == target:
            return right

        return -1

# Time complexity: O(log(n))
# Space complexity: O(1)


class TestBinarySearch:
    def test(self):
        s = Solution()
        arr = [1, 2, 3, 3, 3, 3, 3, 3, 4, 7, 9]
        assert s.binary_search(arr, 3) == 2


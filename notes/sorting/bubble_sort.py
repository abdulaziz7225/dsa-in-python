from typing import List


class Solution:
    def bubble_sort(self, array: List[int]) -> None:
        n = len(array)
        for i in range(n - 1):
            swapped = False

            for j in range(n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True

            if not swapped:
                break

# Time complexity: O(n^2)
# Space complexity: O(1)


class TestBubbleSort:
    def test(self):
        s = Solution()
        arr = [34, 25, 8, 79, 22, 13]
        s.bubble_sort(arr)
        assert arr == [8, 13, 22, 25, 34, 79]

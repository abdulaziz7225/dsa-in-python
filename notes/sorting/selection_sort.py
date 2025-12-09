from typing import List


class Solution:
    def selection_sort(self, array: List[int]) -> None:
        n = len(array)
        for i in range(n - 1):
            min_index = i

            for j in range(i + 1, n):
                if array[j] < array[min_index]:
                    min_index = j

            array[i], array[min_index] = array[min_index], array[i]

# Time complexity: O(n^2)
# Space complexity: O(1)


class TestSelectionSort:
    def test(self):
        s = Solution()
        arr = [64, 25, 12, 22, 11]
        s.selection_sort(arr)
        assert arr == [11, 12, 22, 25, 64]

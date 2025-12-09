from typing import List


class Solution:
    def insertion_sort(self, array: List[int]) -> None:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1

            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = key

# Time complexity: O(n^2)
# Space complexity: O(1)


class TestInsertionSort:
    def test(self):
        s = Solution()
        arr = [22, 16, 12, 15, 29, 39]
        s.insertion_sort(arr)
        assert arr == [12, 15, 16, 22, 29, 39]

from typing import List


class Solution:
    def partition(self, array: List[int], low: int, high: int):
        pivot = array[high]
        i = low - 1

        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                # Swap array[i] and array[j]
                array[i], array[j] = array[j], array[i]

        # Swap array[i+1] and array[high] (or pivot)
        array[i + 1], array[high] = array[high], array[i + 1]

        return i + 1

    def quick_sort(self, array: List[int], low: int, high: int):
        """
        Main function that implements quick sort
        """
        if low < high:
            # p_index is partitioning index, array[p_index] is now at right place
            p_index = self.partition(array, low, high)

            # Recursively sort elements before partition and after partition
            self.quick_sort(array, low, p_index - 1)
            self.quick_sort(array, p_index + 1, high)

# Time Complexity
# Best Case: O(n * log(n))
# Worst Case: O(n^2)
# Space Complexity:
# Best Case: O(log(n))
# Worst Case: O(n)


class TestQuickSort:
    def test(self):
        s = Solution()
        arr = [10, 80, 30, 90, 40, 50, 70]
        s.quick_sort(arr, 0, len(arr) - 1)
        assert arr == [10, 30, 40, 50, 70, 80, 90]

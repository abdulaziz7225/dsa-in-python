from typing import List


class Solution:
    def merge(self, array: List[int], left: int, middle: int, right: int) -> None:
        """
        Merges two subarrays of array[].
        First subarray is array[left..middle]
        Second subarray is arr[middle + 1..right]
        """
        n1 = middle - left + 1
        n2 = right - middle

        # Create temporary arrays
        left_array = array[left:left + n1]
        right_array = array[middle + 1:middle + n2 + 1]

        # Merge the temporary arrays back into array[left..right]
        i = j = 0
        k = left
        while i < n1 and j < n2:
            if left_array[i] < right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1

        # Copy remaining elements of left array if any
        while i < n1:
            array[k] = left_array[i]
            i += 1
            k += 1

        # Copy remaining elements of right array if any
        while j < n2:
            array[k] = right_array[j]
            j += 1
            k += 1

    def sort(self, array: List[int], left: int, right: int) -> None:
        """
        Main function that sorts array[left..right] using merge()
        """
        if left < right:
            middle = (left + right) // 2

            # Recursively sort the first and second halves
            self.sort(array, left, middle)
            self.sort(array, middle + 1, right)

            # Merge the sorted halves
            self.merge(array, left, middle, right)

# Time complexity: O(n * log(n))
# Space complexity: O(n)


class TestMergeSort:
    def test(self):
        s = Solution()
        arr = [12, 3, 72, 5, 61, 8]
        s.sort(arr, 0, len(arr) - 1)
        assert arr == [3, 5, 8, 12, 61, 72]

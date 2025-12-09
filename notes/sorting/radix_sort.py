from typing import List


class Solution:
    def counting_sort(self, array: List[int], exponent: int) -> None:
        result = [0] * len(array)
        count = [0] * 10

        # Count each digit
        for i in range(len(array)):
            index = (array[i] // exponent) % 10
            count[index] += 1

        # Accumulate count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the result array
        i = len(array) - 1
        while i >= 0:
            index = (array[i] // exponent) % 10
            result[count[index] - 1] = array[i]
            count[index] -= 1
            i -= 1

        for i in range(len(array)):
            array[i] = result[i]

    def radix_sort(self, array: List[int]) -> None:
        max_value = max(array)
        exp = 1
        while max_value // exp > 0:
            self.counting_sort(array, exp)
            exp *= 10

# n = number of elements, b = base of numbering system (b = 10 for decimal numbers)
# d = number of digits in the largest number
# Time complexity: Od * (n + b))
# Space complexity: O(n + b)


class TestRadixSort:
    def test(self):
        s = Solution()
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        s.radix_sort(arr)
        assert arr == [2, 24, 45, 66, 75, 90, 170, 802]

from typing import List


class Solution:
    def counting_sort(self, array: List[int]) -> None:
        maximum = max(array)
        count = [0] * (maximum + 1)
        result = [0] * len(array)

        # Count each element
        for num in array:
            count[num] += 1

        # Accumulate count
        for i in range(1, len(count)):
            count[i] += count[i - 1]

        # Build the result array
        for num in array:
            result[count[num] - 1] = num
            count[num] -= 1

        return result

# n = number of elements, k = range of the input
# Time complexity: O(4 * n + 2 * k) ==> O(n + k)
# Space complexity: O(n + k)


class TestCountingSort:
    def test(self):
        s = Solution()
        arr = [12, 3, 18, 3, 9, 9, 0, 14, 7, 12, 3, 11, 8, 6,
               15, 2, 19, 7, 5, 14, 2, 9, 4, 6, 1, 10, 8, 16, 0, 13]
        sorted_arr = s.counting_sort(arr)
        assert sorted_arr == [0, 0, 1, 2, 2, 3, 3, 3, 4, 5, 6, 6, 7,
                              7, 8, 8, 9, 9, 9, 10, 11, 12, 12, 13, 14, 14, 15, 16, 18, 19]

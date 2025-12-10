from typing import List


class Solution:
    def bucket_sort(self, array: List[int]) -> None:
        n = len(array)
        buckets = [[] for _ in range(n)]

        # Add elements into the buckets
        for elem in array:
            # Assuming the elements are from 0 to 1
            bucket_index = int(n * elem)
            buckets[bucket_index].append(elem)

        # Sort each bucket
        for i in range(n):
            buckets[i].sort()

        index = 0
        for bucket in buckets:
            for elem in bucket:
                array[index] = elem
                index += 1

# n = len(array), k = number of buckets
# Time complexity: O(n + n^2 / k + k)
# Space complexity: O(n + k)


class TestBucketSort:
    def test(self):
        s = Solution()
        arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
        print(arr)
        s.bucket_sort(arr)
        print(arr)
        assert arr == [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897]

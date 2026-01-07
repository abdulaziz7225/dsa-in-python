from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def levelOrderTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        result = []

        queue.append(root)
        curr_level = 0

        while queue:
            level_size = len(queue)
            result.append([])

            for _ in range(level_size):
                node = queue.popleft()
                result[curr_level].append(node.value)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            curr_level += 1

        return result

# Time complexity: O(n)
# Space complexity: O(n)


class TestLevelOrderTraversal:
    def test_level_order_traversal(self):
        #          5
        #        /   \
        #      12     13
        #     /  \     \
        #    7    14    2
        #  /  \  /  \  / \
        # 17  23 27 3 8  11

        root = TreeNode(5)
        root.left = TreeNode(12)
        root.right = TreeNode(13)

        root.left.left = TreeNode(7)
        root.left.right = TreeNode(14)

        root.right.right = TreeNode(2)

        root.left.left.left = TreeNode(17)
        root.left.left.right = TreeNode(23)

        root.left.right.left = TreeNode(27)
        root.left.right.right = TreeNode(3)

        root.right.right.left = TreeNode(8)
        root.right.right.right = TreeNode(11)

        s = Solution()
        result = s.levelOrderTraversal(root)

        assert result == [
            [5],
            [12, 13],
            [7, 14, 2],
            [17, 23, 27, 3, 8, 11],
        ]

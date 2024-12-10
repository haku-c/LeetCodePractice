# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        counts = Counter()
        res = []

        def dfs(node):
            if node is None:
                return "#"
            l = dfs(node.left)
            r = dfs(node.right)
            subtree = str(node.val) + "/" + l + "/" + r
            counts[subtree] += 1
            if counts[subtree] == 2:
                res.append(node)
            return subtree

        dfs(root)
        return res

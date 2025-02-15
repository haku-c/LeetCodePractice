# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).


# If two nodes are in the same row and column, the order should be from left to right.


# dfs with sorting
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = defaultdict(list)

        def dfs(node, col, level):
            if node is None:
                return
            self.res[col].append((level, node.val))
            dfs(node.left, col - 1, level + 1)
            dfs(node.right, col + 1, level + 1)

        dfs(root, 0, 0)
        # itemgetter here used to ensure sort is stable
        return [
            ([y for _, y in sorted(self.res[k], key=itemgetter(0))])
            for k in sorted(self.res.keys())
        ]


# bfs solution without sorting

# the key insight is if you know the range of the columns (say -2 to 1), we can just iterate in that range
# it's a bit easier to do bfs since bfs guarantees a level order traversal.

# class Solution:
#     def verticalOrder(self, root: TreeNode) -> List[List[int]]:
#         if root is None:
#             return []

#         columnTable = defaultdict(list)
#         min_column = max_column = 0
#         queue = deque([(root, 0)])

#         while queue:
#             node, column = queue.popleft()

#             if node is not None:
#                 columnTable[column].append(node.val)
#                 min_column = min(min_column, column)
#                 max_column = max(max_column, column)

#                 queue.append((node.left, column - 1))
#                 queue.append((node.right, column + 1))

#         return [columnTable[x] for x in range(min_column, max_column + 1)]

# here's the above bfs solution with the range trick:

# class Solution:
#     def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         self.res = defaultdict(list)
#         self.minCol = 0
#         self.maxCol = -1

#         def dfs(node, col, level):
#             if node is None:
#                 return
#             self.res[col].append((level, node.val))
#             self.minCol = min(self.minCol, col)
#             self.maxCol = max(self.maxCol, col)
#             dfs(node.left, col - 1, level + 1)
#             dfs(node.right, col + 1, level + 1)

#         dfs(root, 0, 0)
#         return [
#             ([y for _, y in sorted(self.res[k], key=itemgetter(0))])
#             for k in range(self.minCol, self.maxCol + 1)
#         ]

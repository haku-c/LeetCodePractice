"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def diameter(self, root: "Node") -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        self.res = 0

        def dfs(node):
            secondLargest = 0
            largest = 0
            for dest in node.children:
                pathLen = 1 + dfs(dest)
                if pathLen > largest:
                    secondLargest = largest
                    largest = pathLen
                elif pathLen > secondLargest:
                    secondLargest = pathLen
            self.res = max(self.res, largest + secondLargest)
            return largest

        dfs(root)
        return self.res


# Given a root of an N-ary tree, you need to compute the length of the diameter of the tree.

# The diameter of an N-ary tree is the length of the longest path between any two nodes in the tree. This path may or may not pass through the root.

# (Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value.)

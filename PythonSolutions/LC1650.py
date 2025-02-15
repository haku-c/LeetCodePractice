"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

from collections import deque

# Given two nodes of a binary tree p and q, return their lowest common ancestor (LCA).

# Each node will have a reference to its parent node. The definition for Node is below:

# class Node {
#     public int val;
#     public Node left;
#     public Node right;
#     public Node parent;
# }

# According to the definition of LCA on Wikipedia:
# "The lowest common ancestor of two nodes p and q in a tree T is the lowest node that has both p and q as descendants (where we allow a node to be a descendant of itself)."


class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        def dfs(current, target):
            if current is None:
                return False
            if current.val == target.val:
                return True
            return dfs(current.left, target) or dfs(current.right, target)

        # case where one is the parent of the other
        if dfs(p, q):
            return p
        if dfs(q, p):
            return q

        seen = set()
        q = deque([q, p])
        # can use a bfs or dfs for this
        while q:
            current = q.popleft()
            if current:
                if current.val in seen:
                    return current
                seen.add(current.val)
                q.append(current.parent)

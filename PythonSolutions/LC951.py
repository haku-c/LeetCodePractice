# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # construct a dictionary of the parents of each node in tree1 and tree2
        parents1 = {}
        parents2 = {}

        def traverse(node, parent, parents):
            if node is None:
                return
            parents[node.val] = parent
            traverse(node.left, node.val, parents)
            traverse(node.right, node.val, parents)

        # handle edge cases involving null roots or roots that are not equal (case of 2 trees where roots different)
        if root1 is None and root2 is None:
            return True
        if (
            (root1 is None and root2 is not None)
            or (root1 is not None and root2 is None)
            or (root1.val != root2.val)
        ):
            return False
        traverse(root1, root1.val, parents1)
        traverse(root2, root2.val, parents2)
        return parents1 == parents2

        # here is a solution where you can do the comparisons directly and use less memory.
        # although more performant, it perhaps is a bit less readable, but also works.
        # def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        # if root1 is None and root2 is None:
        #     # print("leaf node")
        #     return True
        # if not root1 or not root2:
        #     # print("one is None")
        #     return False
        # print(root1.val, root2.val)

        # return root1.val == root2.val and (
        #     (
        #         self.flipEquiv(root1.left, root2.right)
        #         and self.flipEquiv(root1.right, root2.left)
        #     )
        #     or (
        #         self.flipEquiv(root1.left, root2.left)
        #         and self.flipEquiv(root1.right, root2.right)
        #     )
        # )

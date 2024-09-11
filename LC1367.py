# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        lst = []
        # the class variable res is needed here to give a global var
        self.res = False
        current = head
        while current:
            lst.append(current.val)
            current = current.next
        n = len(lst)

        def check(node, ind):
            if not node:
                return
            if node.val == lst[ind]:
                if ind == n - 1:
                    self.res = True
                else:
                    check(node.left, ind + 1)
                    check(node.right, ind + 1)

        def traverse(node):
            # stop traversing if we found an existing path or we reached a leaf.
            if not node or self.res:
                return
            if node.val == lst[0]:
                if n == 1:
                    self.res = True
                    return
                check(node.left, 1)
                check(node.right, 1)
            traverse(node.right)
            traverse(node.left)

        traverse(root)
        return self.res

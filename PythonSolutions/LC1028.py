# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# traverse the string and track which part of the string you are looking at
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        length = len(traversal)

        def dfs(segmentStart, depth):
            # if you reach the end of the tree, return
            if segmentStart >= length:
                return None, segmentStart, -1

            # parse until you get the number
            end = segmentStart + 1
            while end < length and traversal[end].isdigit():
                end += 1

            # assign the current node to the number
            val = int(traversal[segmentStart:end])
            current = TreeNode(val)
            # print("depth " + str(depth))
            # print(val)

            # check if you should continue growing the tree down to the left
            dashCount = 0
            while end < length and traversal[end] == "-":
                dashCount += 1
                end += 1

            if dashCount <= depth:
                return current, end, dashCount

            # grow left
            n1, rightStart, depth1 = dfs(end, depth + 1)
            current.left = n1

            # if depth1 < depth, the next segment needs you to go back up the tree
            if depth1 < depth + 1:
                return current, rightStart, depth1

            # grow right
            n2, index, depth2 = dfs(rightStart, depth1)
            current.right = n2

            return current, index, depth2

        # recursive call and return root
        return dfs(0, 0)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        cache = {}
        self.maxHeight = 0

        # a key thing to note is we update the current height BEFORE we update the max height.
        # consider there is one greatest height path like (1-3-4). The max height before we get to the 4 is one.
        # if we remove the subtree rooted at 4, then the actual answer should be 1.
        # however, we update the max height to become 2 and assign the cache values for 2 to be 2. This is because if we remove
        # the subtree rooted at 2, it leaves the actual max height unaffected, since 2 is not on the max height path
        # notice the algorithm also only ever assigns a max height of 1 to the node 3.
        # if we remove 3, the new max height is 1 because of the path 1-2 that exists.
        # you can think of the algorithm as "carrying over" max height from previous bfs. If there is a greater max height seen before, then removing the current node (and its children) doesn't matter to the max height since there was a longer path
        # just seen.

        # the reason you need to traverse multiple times (one left to right, one right to left) is because if the max height
        # path is in the subtree to the right, you havent yet encountered it due to the ordering of preorder. So you should go the other way in another pass to confirm if there is a longer path or not (remember the concept of "carrying over" a max height)
        # 1
        # /\
        # 2 3
        # - - \
        # - -  4
        def preOrderLeftRight(node, height):
            if node is None:
                return
            if node.val not in cache or cache[node.val] < self.maxHeight:
                cache[node.val] = self.maxHeight
            self.maxHeight = max(self.maxHeight, height)
            preOrderLeftRight(node.left, height + 1)
            preOrderLeftRight(node.right, height + 1)

        def preOrderRightLeft(node, height):
            if node is None:
                return
            cache[node.val] = max(self.maxHeight, cache[node.val])
            self.maxHeight = max(self.maxHeight, height)
            preOrderRightLeft(node.right, height + 1)
            preOrderRightLeft(node.left, height + 1)

        preOrderLeftRight(root, 0)
        self.maxHeight = 0
        preOrderRightLeft(root, 0)
        res = []
        for query in queries:
            res.append(cache[query])
        return res

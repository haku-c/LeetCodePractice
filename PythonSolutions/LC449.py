# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import defaultdict

# the approach here is to do a level order traversal and then insert using the bst rules.
# because the bst invariant holds, if we insert the values such that nodes at lower levels are inserted first, we will get the same tree back


# consider
# the following trees are valid bsts, but are different trees. By inserting in levels of the tree, we can preserve the desired structure
#   2             3       1
#  / \   vs      /         \
# 1   3        2    vs      2
#             /              \
#            1                3
class Codec:
    def __init__(self):
        self.tree = defaultdict(list)

    def levelOrder(self, node, level):
        if node is None:
            return
        self.tree[level].append(node.val)
        self.levelOrder(node.left, level + 1)
        self.levelOrder(node.right, level + 1)

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        self.levelOrder(root, 0)
        # print(self.tree)
        res = ""
        for lst in self.tree.values():
            current = []
            for i in lst:
                current.append(str(i))
            current = ",".join(current)
            res += current + ";"
        # print(res)
        self.tree = defaultdict(list)
        return res

    def insert(self, value, current):
        if current is None:
            return
        if value < current.val and current.left is None:
            current.left = TreeNode(value)
            return
        elif value > current.val and current.right is None:
            current.right = TreeNode(value)
            return
        elif value > current.val:
            self.insert(value, current.right)
        else:
            self.insert(value, current.left)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""

        d = data.split(";")
        root = None
        if d[0] != "":
            root = TreeNode(int(d[0]))
        for string in d[1:]:
            currentLevel = string.split(",")
            for i in currentLevel:
                if i != "":
                    self.insert(int(i), root)
        return root


# different version using a bfs for the level order and directly creates the string

# class Codec:
#     def serialize(self, root: Optional[TreeNode]) -> str:
#         """Encodes a tree to a single string."""
#         if root is None:
#             return ""
#         res = ""
#         lvl = 0
#         queue = [(0, root)]
#         while queue:
#             currentLevel, currentNode = queue.pop()
#             if currentLevel > lvl:
#                 res += ";"
#                 lvl += 1
#             elif lvl > 0:
#                 res += ","
#             res += str(currentNode.val)
#             if currentNode.left:
#                 queue.append((currentLevel + 1, currentNode.left))
#             if currentNode.right:
#                 queue.append((currentLevel + 1, currentNode.right))

#         return res

#     def insert(self, value, current):
#         if value < current.val and not current.left:
#             current.left = TreeNode(value)
#             return
#         elif value > current.val and not current.right:
#             current.right = TreeNode(value)
#             return
#         elif value > current.val:
#             self.insert(value, current.right)
#         else:
#             self.insert(value, current.left)

#     def deserialize(self, data: str) -> Optional[TreeNode]:
#         """Decodes your encoded data to tree."""
#         if data == "":
#             return None
#         d = data.split(";")
#         root = TreeNode(int(d[0]))
#         for string in d[1:]:
#             for i in string.split(","):
#                 self.insert(int(i), root)
#         return root

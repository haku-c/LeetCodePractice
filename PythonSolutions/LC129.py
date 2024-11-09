class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def traverse(node, current):
            if node.left is not None and node.right is not None:
                current = current + str(node.val)
                self.res += int(current)
                return
            current = current + str(node.val)
            if node.left:
                traverse(node.left, current)
            if node.right:
                traverse(node.right, current)

        traverse(root, "")
        return self.res


# prefix ordering for this question
# note the use of the class variable

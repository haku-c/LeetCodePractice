def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    hs = set(to_delete)
    if root.val not in hs:
        res = [root]
    else:
        res = []

    def recurse(current):
        if not current:
            return None
        current.left = recurse(current.left)
        current.right = recurse(current.right)
        # if this node is not forbidden, we can just keep the node there
        if current.val not in hs:
            return current
        if current.left:
            res.append(current.left)
        if current.right:
            res.append(current.right)
        # otherwise the node is forbidden, None is returned, and the node is deleted.

    recurse(root)
    return res

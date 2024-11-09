def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
    hs = set(to_delete)
    if root.val not in hs:
        res = [root]
    else:
        res = []

    def recurse(current):
        if not current:
            return None
        # it is important to do the assignment of the attribute. If we do current = None or something similar, this only changes the local variable and leaves the original tree unchanged.
        current.left = recurse(current.left)
        current.right = recurse(current.right)
        # if this node is not forbidden, we can just keep the node there
        if current.val not in hs:
            return current
        # otherwise the current node is forbidden, and we should add the children to the result as they are the start of a tree in the forest
        if current.left:
            res.append(current.left)
        if current.right:
            res.append(current.right)
        # otherwise the node is forbidden, None is returned, and the node is deleted.

    recurse(root)
    return res

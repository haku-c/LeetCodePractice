class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
    nodes = {}
    notRoot = set()
    for parent, child, left in descriptions:
        if not child in nodes:
            nodes[child] = TreeNode(child, None, None)
        if not parent in nodes:
            nodes[parent] = TreeNode(parent, None, None)
        if left:
            nodes[parent].left = nodes[child]
        else:
            nodes[parent].right = nodes[child]
        notRoot.add(child)
    for num, node in nodes.items():
        if num not in notRoot:
            return node


# you could use a tuple to store at each dictionary entry the node and if that node is a child or not, but that appears
# to be slower than just querying a set.

public class LC1372 {

    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        TreeNode() {
        }

        TreeNode(int val) {
            this.val = val;
        }

        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public int helper(TreeNode current, int direction, int nodes) {
        if (current == null) {
            return nodes;
        }
        // direction = 1 indicates you go right to continue the zig zag, left o.w
        if (direction == 1) {
            return Math.max(Math.max(helper(current.right, 0, nodes + 1), helper(current.left, 1, 0)), nodes);
        } else {
            return Math.max(Math.max(helper(current.left, 1, nodes + 1), helper(current.right, 0, 0)), nodes);
        }
    }

    public int longestZigZag(TreeNode root) {
        return Math.max(helper(root.right, 0, 0), helper(root.left, 1, 0));
    }
}

// this solution uses recursion
// we have a choice to either go left or right from the root node. Pick the choice which results in the max value.
// in our helper function, we can either choose to continue with the current zig-zag direction (add 1 to node count), start a new zig zag
// continue going in the same direction (count set to 0), or the current node count is the highest amount

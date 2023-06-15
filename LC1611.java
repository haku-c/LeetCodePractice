import java.util.ArrayList;

public class LC1611 {
    ArrayList<Integer> levels = new ArrayList<>();

    public int maxLevelSum(TreeNode root) {
        int index = 0;
        sumLevel(root, 0);
        int max = levels.get(0);
        for (int i = 1; i < levels.size(); i++) {
            if (levels.get(i) > max) {
                max = levels.get(i);
                index = i;
            }
        }

        return index + 1;
    }

    public void sumLevel(TreeNode curr, int level) {
        if (curr == null) {
            return;
        }
        if (levels.size() <= level) {
            levels.add(curr.val);
        } else {
            levels.set(level, levels.get(level) + curr.val);
        }
        sumLevel(curr.right, level + 1);
        sumLevel(curr.left, level + 1);

    }
}

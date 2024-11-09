import java.util.*;

public class LC39 {
    List<List<Integer>> res;

    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        res = new ArrayList<>();
        helper(candidates, target, new ArrayList<>(), 0);
        return res;
    }

    public void helper(int[] candidates, int target, List<Integer> currentNumbers, int index) {
        // return if you run out of elements
        if (index >= candidates.length) {
            return;
        }
        if (target == 0) {
            res.add(new ArrayList(currentNumbers));
            return;
        }
        // because we go in order and elements are distinct, we don't have to worry about repeating permutations
        // check if you could add before you recurse
        if (candidates[index] <= target) {
            currentNumbers.add(candidates[index]);
            helper(candidates, target - candidates[index], currentNumbers, index);
            // must remove the last element you added before you recurse to ensure you don't accidentally add twice in 1 recursive call
            currentNumbers.remove(currentNumbers.size() - 1);
        }
        // go to the next index if you can't
        helper(candidates, target, currentNumbers, index + 1);
    }
}

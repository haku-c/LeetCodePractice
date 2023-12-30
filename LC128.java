import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;

public class LC128 {
    HashSet<Integer> set = new HashSet<>();

    public int longestConsecutive(int[] nums) {
        int res = 0;
        for (int i : nums) {
            set.add(i);
        }
        Arrays.sort(nums);
        for (int i = 0; i < nums.length; i++) {
            if (set.contains(nums[i])) {
                res = Math.max(helper(set, nums[i]), res);
            }
        }
        return res;
    }

    public static int helper(HashSet<Integer> set, int start) {
        set.remove(start);
        int count = 1;
        start = start + 1;
        while (set.contains(start)) {
            set.remove(start);
            count++;
            start++;
        }
        return count;
    }
}

// ordering: sort the list. if you come across a portion of a sequence you already accounted for, all those values are removed from the set already
// this reduces recomputation



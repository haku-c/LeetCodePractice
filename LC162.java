public class LC162 {
    public int findPeakElement(int[] nums) {
        if (nums.length == 1) return 0;
        return binarySearch(0, nums.length - 1, nums);
    }

    public int binarySearch(int start, int end, int[] nums) {
        int index = start + (-start + end) / 2;
        if ((index > 0 && index < nums.length - 1 && nums[index - 1] < nums[index] && nums[index] > nums[index + 1])
                || (index == 0 && nums[index + 1] < nums[index]) || (index == nums.length - 1 && nums[index - 1] < nums[index])) {
            return index;
        } else if (index > 0 && nums[index - 1] > nums[index]) {
            return binarySearch(start, index - 1, nums);
        } else {
            return binarySearch(index + 1, end, nums);
        }
    }

    // mid = start + (end - start) / 2 to prevent overflow errors
    /*
    linear
        int[] temp = new int[nums.length + 2];
        temp[0] = Integer.MIN_VALUE;
        temp[temp.length] = Integer.MIN_VALUE;
        for (int i = 1; i < nums.length + 1; i++) {
            if (nums[i] < nums[i - 1] && nums[i] < nums[i + 1]) {
                return i;
            }
        }
        return -1;*/
    /*
     * recursion: check midpoint. Since endpoints can have peaks, if we run alg on the side with a greater value than mid, it must have a peak somewhere
     * (just increasing uniformly leads to a peak on the end) */

}

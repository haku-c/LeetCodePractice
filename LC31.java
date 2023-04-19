import java.util.Arrays;

public class LC31 {
    public void nextPermutation(int[] nums) {
        int index1 = nums.length - 1;
        int index2 = nums.length - 1;
        while (index1 > 0) {
            if (nums[index1] > nums[index1 - 1]) {
                index1 = index1 - 1;
                break;
            }
            index1--;
        }

        while (index2 > 0) {
            if (nums[index2] > nums[index1]) {
                break;
            }
            index2--;
        }
        if (index1 == 0 && index2 == 0) {
            Arrays.sort(nums);
            return;
        }
        // if the range is not already sorted, swap the two
        int temp = nums[index1];
        nums[index1] = nums[index2];
        nums[index2] = temp;
        Arrays.sort(nums, index1 + 1, nums.length);
    }
}

// swap two numbers
// when you have to replace on the left-most, rearrange the remaining numbers in ascending order
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4:
            return 0
        return min(
            min(nums[len(nums) - 4] - nums[0], nums[len(nums) - 1] - nums[3]),
            min(nums[len(nums) - 3] - nums[1], nums[len(nums) - 2] - nums[2]),
        )


# there are 4 scenarios once you find the 3 smallest and 3 largest numbers
# n1 n2 n3 n4 ... n6 n7 n8 n9 (sorted)
# scenario 1: n1 -> n9, n2 -> n9, n3 -> n9. then the result is n9 - n4
# scenario 2: n1 -> n9, n2 -> n9, n9 -> n3. then the result is n8 - n3
# scenario 3: n1 -> n9, n9 -> n2, n8 -> n2. then the result is n7 - n2
# scenario 4: n9 -> n2, n8 -> n2, n7 -> n2. then the result is n6 - n1

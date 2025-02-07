class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        current = 0
        prev = nums[current]
        start = current
        for _ in range(n):
            new = nums[(current + k) % n]
            nums[(current + k) % n] = prev
            prev = new
            current = (current + k) % n
            if current == start:
                current = (current + 1) % n
                prev = nums[current]
                start = current


# you can also do 3 reversals
# reverse the whole array reverse the first k elements
# reverse the last tail k - 1 elements

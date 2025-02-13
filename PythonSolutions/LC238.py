class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        backwards = [0] * n
        backwards[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            backwards[i] = nums[i] * backwards[i + 1]

        forwards = nums[0]
        backwards[0] = backwards[1]
        for i in range(1, n - 1):
            backwards[i] = backwards[i + 1] * forwards
            forwards *= nums[i]
        backwards[-1] = forwards
        return backwards


# in order to not use division, you keep the products of the segments to the right and to the left of the current index
# then multiply
# cache results going from the right to the left (to use less space we store this in the eventual result array)
# then as we go from left to right, we track the left to right product (forwards) aka the left segment in one variable

# there's some annoying code dealing with the edges of the result

# this problem isn't actually as contrived as you might think. Consider an array with 0s. If you wanted to use division, you would
# run into a div by zero and not actually be able to solve the problem!

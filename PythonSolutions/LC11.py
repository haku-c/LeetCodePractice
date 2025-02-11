class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max, right_max = 0, 0
        res = 0
        while left < right:
            if height[left] < height[right]:
                res = max(res, height[left] * (right - left))
                left += 1
            else:
                res = max(res, height[right] * (right - left))
                right -= 1
        return res

    # the answer relies on the smallest of the two ends in the result
    # start with two pointers on either end
    # if the left height is smaller than the right, try to find a larger height by moving the left pointer
    # same idea applies for the right height
    # we wouldnt want to shrink the righthand side if left is smaller since that would guarantee the next segment explored
    # is smaller -> the amount of volume enclosed is limited by the left height, not the right height; even if
    # height[right-1] > height[right], the volume enclosed decreases, since height[left] < height[right-1]

    # whereas the exploration as explained could still potentially find better results

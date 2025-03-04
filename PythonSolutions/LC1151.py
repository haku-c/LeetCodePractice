class Solution:
    def minSwaps(self, data: List[int]) -> int:
        size = sum(data)
        start = 0
        window = sum(data[start : start + size])
        res = size - window
        while start < len(data) - size:
            window -= data[start]
            window += data[start + size]
            res = min(res, size - window)
            start += 1
        return res


# sliding window solution

# we are trying to find the window in the array which has the least amount of 0s.
# the window size is equal to the number of ones in the entire array.
# this way, we can just move any ones outside the window into the window by swapping those ones with the 0s in the window.

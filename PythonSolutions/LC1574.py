class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        # start represents the last index of the leftmost increasing contiguous subarray
        start = -1
        for i in range(n - 1):
            if arr[i + 1] < arr[i]:
                start = i
                break
        # if this is increasing the entire way, nothing needs to be removed.
        if start == -1:
            return 0

        end = n - 1
        res = n - start - 1
        while start < end and start >= 0:
            while arr[end - 1] >= arr[start] and arr[end] >= arr[end - 1] and end > 0:
                end -= 1
            if arr[end] >= arr[start]:
                res = min(res, end - start - 1)
            start -= 1

        # this check is for examples like 8,8,1,2,3
        while end > 0 and arr[end - 1] <= arr[end]:
            end -= 1
            res = min(res, end)
        return res


# it's better to do the two pointers where start = 0 and end is the furthest left index to start the rightmost increasing subarray
# for example: 8,7,6,1,2,3 you want end to be 3 initially since 1,2,3 is an increasing subarray
# then when you search, you increment both start and end instead of decrementing.
# the decrementing approach leaves you having to have the last check in the code

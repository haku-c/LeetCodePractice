class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)

        sweep = []
        start = 0
        for i in range(1, n):
            if nums[i - 1] % 2 == nums[i] % 2:
                sweep.append((start, i - 1))
                start = i
        sweep.append((start, n))
        res = []

        def search(lst, target):
            start = 0
            end = len(lst) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if lst[mid][0] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            return end

        for start, end in queries:
            ind = search(sweep, start)
            left, right = sweep[ind]
            if start >= left and end <= right:
                res.append(True)
            else:
                res.append(False)
        return res


# the above solution uses a sweep approach and binary search. Log intervals that are valid and then search to see if the interval
# in the query is valid


# the below solution uses a prefix sum counting the number of invalid pairs from 0 to i at prefix[i]
# if the number of invalid pairs does not change from start to end, then we know that the specified range is valid.
# pay attention to indexing; we don't need to do anything fancy to account for the 0 index (no possible pairs formed with just nums[0])
class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
        prefix = [0] * n
        count = 0
        for i in range(1, n):
            if (nums[i] % 2) == (nums[i - 1] % 2):
                count += 1
            prefix[i] = count
        res = []
        for start, end in queries:
            res.append((prefix[end] == prefix[start]))
        return res

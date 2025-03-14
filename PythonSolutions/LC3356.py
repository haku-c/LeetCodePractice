class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        diffArr = [0] * (len(nums) + 1)
        pref = 0
        res = 0
        for i in range(len(nums)):
            while pref + diffArr[i] < nums[i]:
                res += 1
                if res > len(queries):
                    return -1

                l, r, v = queries[res - 1]
                # apply the query update. Either we can apply the query update at index i (if i >= l) or we apply it later on when i < l
                if i < l:
                    diffArr[l] += v
                    diffArr[r + 1] -= v
                elif l <= i <= r:
                    diffArr[i] += v
                    diffArr[r + 1] -= v
                # if i > r, then this query is not relevant, since it does not fix any new indices
            pref += diffArr[i]
        return res

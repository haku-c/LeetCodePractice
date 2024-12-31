import heapq


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        lst = [(y, x) for x, y in list(enumerate(nums))]
        heapq.heapify(lst)
        for i in range(k):
            current, index = heapq.heappop(lst)
            heapq.heappush(lst, (current * multiplier, index))
        res = [0] * (len(nums))
        for val, ind in lst:
            res[ind] = val
        return res


# more heap usage!

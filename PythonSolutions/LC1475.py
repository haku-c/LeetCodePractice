from collections import deque
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n = len(prices)
        stack = deque()
        res = prices.copy()
        for i in range(n):
            while stack and stack[-1][0] >= prices[i]:
                price,index = stack.pop()
                res[index] -= prices[i]
            stack.append((prices[i],i))
        return res
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = [0] * (n + 1)
        counts = [0] * (n + 1)
        for i in range(0, n):
            a = A[i]
            b = B[i]
            res[i + 1] = res[i]
            counts[a] += 1
            if counts[a] == 2:
                res[i + 1] += 1
            counts[b] += 1
            if counts[b] == 2:
                res[i + 1] += 1
        return res[1:]


# just track if you've seen a certain element twice or not. If so, the count increases

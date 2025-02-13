class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def digitSum(num):
            res = 0
            while num > 0:
                res, num = res + num % 10, num // 10
            return res

        counts = defaultdict(list)
        res = -1
        for n in nums:
            s = digitSum(n)
            l = len(counts[s])
            if l == 2:
                if n >= counts[s][1]:
                    counts[s][0], counts[s][1] = counts[s][1], n
                    res = max(res, counts[s][0] + n)
                elif counts[s][0] < counts[s][1]:
                    counts[s][0] = n
                    res = max(res, n + counts[s][1])
            elif l == 1:
                if n > counts[s][0]:
                    counts[s].append(n)
                else:
                    counts[s].append(n)
                    counts[s][0], counts[s][1] = counts[s][1], counts[s][0]
                res = max(res, counts[s][0] + counts[s][1])
            else:
                counts[s].append(n)
        return res


# lots of small tricks for faster runtime: single line assignments, using a swap instead of a prepend, not using sum function instead of a simple add

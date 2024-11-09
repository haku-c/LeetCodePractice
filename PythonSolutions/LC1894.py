# class Solution:
#     def chalkReplacer(self, chalk: List[int], k: int) -> int:
#         n = len(chalk)
#         prefix = [0] * n
#         prefix[0] = chalk[0]
#         for i in range(1, n):
#             prefix[i] = prefix[i - 1] + chalk[i]
#         remainder = k % prefix[n - 1]
#         start = 0
#         end = n - 1
#         # refresher on binary search
#         while start <= end:
#             current = start + (end - start) // 2
#             if prefix[current] < remainder:
#                 start = current + 1
#             elif prefix[current] > remainder:
#                 end = current - 1
#             else:
#                 current = (current + 1) % n
#                 break


#         if prefix[current] > remainder:
#             return current
#         else:
#             return current + 1


# the easy solution
class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        s = sum(chalk)
        remainder = k % s
        for i in range(len(chalk)):
            remainder -= chalk[i]
            if remainder < 0:
                return i

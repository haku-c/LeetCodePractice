class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # backtracking solution (takes much longer)
        # s = set(nums)
        # self.res = ''
        # def backtrack(current):
        #     if len(current) > n:
        #         return
        #     if len(current) == n and current not in s:
        #         self.res = current
        #         return
        #     backtrack(current + '0')
        #     backtrack(current + '1')
        # backtrack('')
        # return self.res

        # iterative version just checking the values of the numbers in the list
        n = len(nums)
        s = list(map(lambda x: int(x, 2), nums))
        for i in range((2**n)):
            if i not in s:
                return bin(i)[2:].zfill(n)

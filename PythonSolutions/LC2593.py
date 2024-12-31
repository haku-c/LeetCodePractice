class Solution:
    def findScore(self, nums: List[int]) -> int:
        marks = [0] * len(nums)
        lst = list(enumerate(nums))
        lst = sorted(lst, key=lambda x: x[1])
        # print(lst)
        res = 0
        for i in range(len(lst)):
            index, value = lst[i]
            if not marks[index]:
                marks[index] = 1
                if index < len(nums) - 1:
                    marks[index + 1] = 1
                if index > 0:
                    marks[index - 1] = 1
                res += value
        return res


# useful to review sorting a list with indices.

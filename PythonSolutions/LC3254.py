class Solution:
    def resultsArray(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        res = [-1] * (n)
        currentValidCount = 0
        for i in range(n):
            currentNumber = arr[i]

            if i >= k and currentValidCount == k:
                currentValidCount -= 1

            if i == 0:
                currentValidCount = 1
            elif currentNumber != arr[i - 1] + 1:
                currentValidCount = 1
            else:
                currentValidCount += 1

            if currentValidCount == k:
                res[i] = currentNumber

        return res[k - 1 :]


# a better decision is to make everything the current value and then set the result array at that index to
# -1 if that condition is not met. This is because it's easier to just check if the array is not ascending

# another clean solution (instead of using the counter you can use a pointer tracking where the current subsequence begins)
# class Solution:
#     def resultsArray(self, nums: list[int], k: int) -> list[int]:
#         results = []
#         start = 0

#         for i in range(len(nums)):
#             if i > 0 and nums[i] != nums[i - 1] + 1:
#                 start = i
#             if i >= k - 1:
#                 if i - start + 1 >= k:
#                     results.append(nums[i])
#                 else:
#                     results.append(-1)

#         return results

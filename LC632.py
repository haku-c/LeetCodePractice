import random


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        self.k = len(nums)
        allNums = []
        for i in range(len(nums)):
            for n in nums[i]:
                allNums.append((n, i))
        allNums = sorted(allNums)
        window = [0] * self.k
        start = 0
        count = 0
        resLeft = 0
        resRight = float("inf")
        for end in range(len(allNums)):
            window[allNums[end][1]] += 1
            if window[allNums[end][1]] == 1:
                count += 1

            while count == len(nums):
                if allNums[end][0] - allNums[start][0] < resRight - resLeft:
                    resRight = allNums[end][0]
                    resLeft = allNums[start][0]

                window[allNums[start][1]] -= 1
                if window[allNums[start][1]] == 0:
                    count -= 1
                start += 1

        return [resLeft, resRight]


# generate some large randomized test cases
# k = 3500
# n = 50
# test = []
# for i in range(k):
#     temp = []
#     for j in range(n):
#         temp.append(random.randint(-(10**5), 10**5))
#     test.append(temp)

# for i in range(len(test)):
#     test[i] = sorted(test[i])

# file1 = open("LC632tests.txt", "w")
# file1.writelines(str(test))
# file1.close()

# self.k = len(nums)
#         res = []
#         for i in range(self.k):
#             nums[i] = set(nums[i])
# self.allNums = sorted(list(set.union(*nums)))
# self.appearances = {}
# for number in self.allNums:
#     current = ""
#     for i in range(self.k):
#         if number in nums[i]:
#             current = "".join([current,"1"])
#         else:
#             current = "".join([current,"0"])
#     self.appearances[number] = current

# def search(self, size):
#     left = 0
#     right = left + size
#     valid = False
#     smallest = float('inf')
#     leftInterval, rightInterval = -1,-1
#     while right <= len(self.allNums):
#         curr = self.appearances[self.allNums[left]]
#         for i in range(left, right):
#             curr = str(int(curr) | int(self.appearances[self.allNums[i]]))
#             if curr == "1" * self.k:
#                 valid = True
#                 if self.allNums[right - 1] - self.allNums[left] < smallest:
#                     leftInterval = self.allNums[left]
#                     rightInterval = self.allNums[right - 1]
#                     smallest = self.allNums[right - 1] - self.allNums[left]
#                 break
#         left += 1
#         right += 1
#     return valid, leftInterval, rightInterval
# # binary search on interval sizes
# start = 1
# end = len(self.allNums)
# currentSize = float('inf')
# resLeft = self.allNums[0]
# resRight = self.allNums[0]
# while start <= end:
#     middle = start + (end - start) // 2
#     valid, left, right = search(self, middle)
#     if valid and currentSize > right - left:
#         resLeft = left
#         resRight = right
#     if valid:
#         end = middle - 1
#     else:
#         start = middle + 1
# return [resLeft, resRight]

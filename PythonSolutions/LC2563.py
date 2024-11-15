import bisect


# this is a binary search-esque solution using bisect, but the below solution using a window is more elegant
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        sortedList = sorted(nums)
        res = 0

        for i in range(n):
            number = sortedList[i]
            # print(number)
            higherInd = bisect.bisect_right(sortedList, upper - number, i + 1)
            # print("higher " + str(higherInd))
            lowerInd = bisect.bisect_left(sortedList, lower - number, i + 1)
            # print("lower " + str(lowerInd))
            res += higherInd - lowerInd
            # print("res " + str(res))
            # print("i " + str(i))

        return res


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums = sorted(nums)

        def count(value):
            start = 0
            end = n - 1
            r = 0
            while start < end:
                s = nums[start] + nums[end]
                if s >= value:
                    end -= 1
                else:
                    r += end - start
                    start += 1
            return r

        return count(upper + 1) - count(lower)


# the number of pairs whose sum <= upper minus the number of pairs whose sum < lower is the number of pairs in the desired range
# count(upper+1) - count(lower) = count(lower <= x <= upper)


def searchRight(lst, value):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        if lst[mid] <= value:
            start = mid + 1
        else:
            end = mid - 1
    return end


def searchLeft(lst, value):
    start = 0
    end = len(lst) - 1
    while start <= end:
        mid = start + ((end - start) // 2)
        if lst[mid] >= value:
            end = mid - 1
        else:
            start = mid + 1
    return start

from collections import Counter


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = Counter(nums)
        countsSequence = Counter()
        for i in range(len(nums)):
            current = nums[i]
            if counts[current] == 0:
                continue
            if countsSequence[current - 1] > 0:
                counts[current] -= 1
                countsSequence[current - 1] -= 1
                countsSequence[current] += 1
            else:
                # we have to build out a sequence of length 3 here
                if counts[current + 1] <= 0 or counts[current + 2] <= 0:
                    return False
                counts[current] -= 1
                counts[current + 1] -= 1
                counts[current + 2] -= 1
                countsSequence[current + 2] += 1

        return True

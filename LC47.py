def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    solutions = []
    size = len(nums)

    def backtrack(dictionary, currentArr):
        if len(currentArr) == size:
            solutions.append(list(currentArr))
            return
        for entry in dictionary:
            if dictionary[entry] > 0:
                currentArr.append(entry)
                dictionary[entry] -= 1
                backtrack(dictionary, currentArr)
                currentArr.pop()
                dictionary[entry] += 1
        return

    d = {}
    for num in nums:
        d.setdefault(num, 0)
        d[num] = d[num] + 1
    backtrack(d, [])
    return solutions


# You need to copy the currentArr since the arguments are pass by reference. Since you mutate the list, the same
# list is being modified in each pass. Then when the list is cleared at the end you get a the same value in each
# entry (empty list)

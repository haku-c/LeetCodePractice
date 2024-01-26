class Solution(object):
    def findMatrix(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        s = {}
        for n in nums:
            if n not in s:
                s[n] = 0
            s[n] += 1
        soln = []
        while len(s) > 0:
            temp = []
            curr = s.items()
            for entry, count in curr:
                if count == 0:
                    s.pop(entry)
                else:
                    temp.append(entry)
                    s[entry] -= 1
            soln.append(temp)
        return soln[0 : len(soln) - 1]

    # can do this in one pass. just use the number of the value stored in the hashmap for that entry as the index of the array you append to

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        last = {}
        first = {}
        for i in range(len(s)):
            char = s[i]
            if char not in first:
                first[char] = i
                continue
            else:
                last[char] = i
        res = 0
        for end in list(last.keys()):
            # temp = set()
            # for i in range(first[end] + 1, last[end]):
            #     temp.add(s[i])
            # res += len(temp)
            res += len(set(s[first[end] + 1 : last[end]]))
        return res


# you can make things faster by using string indexing instead of iterating by character
# this solution leverages the property of 3 length palindromes in that they have pairs of the same char at the end and beginning.

class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        res = [s[0:2]]
        for i in range(2, len(s)):
            if s[i] == s[i - 1] == s[i - 2]:
                continue
            res.append(s[i])
        return "".join(res)


# appending all the strings in a list at once is much faster than appending each character one by one in a loop.

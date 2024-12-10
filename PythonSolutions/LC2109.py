class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # res = []
        # current = 0
        # currentSpace = spaces[current]
        # for i in range(len(s)):
        #     c = s[i]
        #     if i == currentSpace:
        #         res.append(" ")
        #         current += 1
        #         if current < len(spaces):
        #             currentSpace = spaces[current]
        #     res.append(c)
        # return "".join(res)
        res = []
        start = 0
        for space in spaces:
            res.append(s[start:space])
            res.append(" ")
            start = space
        res.append(s[space:])
        return "".join(res)


# the uncommented version is faster and takes up less space
# do note the handling of the first and last space [0:space1] and [spacen:]

from collections import defaultdict


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        lstNum = list(s)
        startEnd = defaultdict(int)

        for start, end, val in shifts:
            if val == 0:
                startEnd[start] += -1
                startEnd[end + 1] += 1
            else:
                startEnd[start] += 1
                startEnd[end + 1] += -1

        current = 0
        startEnd = list(sorted(startEnd.items()))
        track = 0
        for i in range(len(s)):
            if current < len(startEnd) and startEnd[current][0] <= i:
                track += startEnd[current][1]
                current += 1
            lstNum[i] = chr((ord(lstNum[i]) - 97 + track) % 26 + 97)

        return "".join(lstNum)

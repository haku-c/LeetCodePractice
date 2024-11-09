class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        current = ""
        count = 0
        self.counts = [a, b, c]
        letters = ["a", "b", "c"]

        def getLargest():
            return sorted(enumerate(self.counts), reverse=True, key=lambda x: x[1])[0][
                0
            ]

        def getNotThree(currentLetter):
            for i, j in sorted(
                enumerate(self.counts), reverse=True, key=lambda x: x[1]
            ):
                if self.counts[i] > 0 and currentLetter != letters[i]:
                    return i
            return 3

        while not all(i <= 0 for i in self.counts):
            nxt = getLargest()
            if letters[nxt] == current and count == 2:
                nxt = getNotThree(current)
                if nxt == 3:
                    break
                count = 1
            elif letters[nxt] == current:
                count += 1
            else:
                count = 1
            res += letters[nxt]
            current = letters[nxt]
            self.counts[nxt] -= 1
        return res

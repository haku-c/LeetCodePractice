class Solution:
    def smallestNumber(self, pattern: str) -> str:
        used = [False] * 10
        self.res = ""

        def backtrack(index, used, res):
            if index == len(pattern):
                self.res = res
                return True
            for i in range(1, 10):
                if not used[i] and (
                    (pattern[index] == "D" and str(i) < res[-1])
                    or (pattern[index] == "I" and str(i) > res[-1])
                ):
                    used[i] = True
                    if backtrack(index + 1, used, res + str(i)):
                        return True
                    used[i] = False
            return False

        for i in range(1, 10):
            used[i] = True
            if backtrack(0, used, str(i)):
                return self.res
            used[i] = False
        return self.res


# more backtracking
# a good tell is you make a series of decisions and the space is small

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.seen = 0
        self.res = ""
        self.chars = ["a", "b", "c"]

        def backtrack(current):
            if len(current) == n:
                self.seen += 1
                if self.seen == k:
                    self.res = current
                return
            for i in range(3):
                if self.chars[i] != current[-1]:
                    backtrack(current + self.chars[i])
                    if self.res != "":
                        return

        for i in range(3):
            backtrack(self.chars[i])
            if self.res != "":
                return self.res
        return self.res


# backtracking solution with early stopping.
# return the result if we hit k (hence the if checks in the loops)

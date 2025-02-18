class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [-1] * (2 * (n - 1) + 1)
        free = [0] * (n + 1)

        self.res = []

        def place(free, res):
            # all numbers are used
            if free.count(1) == n:
                self.res = res
                return True

            start = 0
            while start < len(res) and res[start] != -1:
                start += 1

            for i in range(n, 0, -1):
                if free[i] == 0:
                    if i == 1:
                        free[i] = 1
                        res[start] = i

                        if place(free, res):
                            return True

                        free[i] = 0
                        res[start] = -1
                    # early stop
                    elif start + i >= (2 * (n - 1) + 1):
                        return False
                    elif start + i < (2 * (n - 1) + 1) and res[start + i] == -1:
                        free[i] = 1
                        res[start] = i
                        res[start + i] = i

                        if place(free, res):
                            return True

                        free[i] = 0
                        res[start] = -1
                        res[start + i] = -1
            return False

        # don't forget to actually call the function, :)
        place(free, res)

        return self.res


# a little trickier backtracking. Treat the one case differently

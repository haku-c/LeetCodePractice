class Solution:
    def minimumSteps(self, s: str) -> int:
        steps = 0
        ones = 0
        for c in s:
            if c == "0":
                steps += ones
            else:
                ones += 1
        return steps

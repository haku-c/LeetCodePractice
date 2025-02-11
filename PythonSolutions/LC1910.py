class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            index = s.index(part)
            s = s[0:index] + s[(index + len(part)) :]
        return s


# the above is the lazy pythonic version which is fast on small inputs (would be quadratic)


# the below is the O(nm) using a stack
# thing to note here is using negative indexing to retrieve the last n elements of the stack
class Solution2:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        n = len(part)
        for c in s:
            stack.append(c)
            if len(stack) >= n and "".join(stack[-n:]) == part:
                for _ in range(n):
                    stack.pop()
        return "".join(stack)

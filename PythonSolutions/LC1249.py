class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        skip = []
        stack = []
        for i in range(len(s)):
            c = s[i]
            if c == "(":
                skip.append(i)
                stack.append("(")
            elif c == ")":
                if len(stack) == 0:
                    skip.append(i)
                else:
                    skip.pop()
                    stack.pop()
        res = []
        start = 0
        for i in skip:
            end = i
            if start < end:
                res.append(s[start:end])
            start = end + 1
        res.append(s[start:])
        return "".join(res)


# this solution uses 2 stacks: 1 tracks '(' needing to be matched
# the other tracks indices of parens that are going to be removed from the result

# we mark an index to be removed in the cases where:
# 1) we have a ')' which can have no corresponding '(' before it, e.g in asd)
# 2) there are no matching ')' remaining for an existing '(' e.g waffles((arecool

# Once we have marked indices for deletion, we can concatenate all the unskipped substrings.
# take chunks of s taking care to skip the marked indices. I use two pointers.
# note the edge case where there are no skips, we take the whole string hence end = -1 initially.

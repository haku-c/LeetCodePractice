# this version is intuitive since we treat wildcards as separate from left or right parens
class Solution:
    def checkValidString(self, s: str) -> bool:
        free = 0
        left = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            if c == "*":
                free += 1
            elif c == "(":
                left += 1
            else:
                if left > 0:
                    left -= 1
                elif free > 0:
                    free -= 1
                else:
                    return False
        if left > free:
            return False
        free = 0
        right = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == "*":
                free += 1
            elif c == ")":
                right += 1
            else:
                if right > 0:
                    right -= 1
                elif free > 0:
                    free -= 1
                else:
                    return False
        if right > free:
            return False
        return True


# in actuality with this approach, we can just treat wildcards as the left paren going left to right
# or the right paren going right to left
class Solution:
    def checkValidString2(self, s: str) -> bool:
        left = 0
        n = len(s)
        for i in range(n):
            c = s[i]
            if c == "*" or c == "(":
                left += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    return False
        right = 0
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c == "*" or c == ")":
                right += 1
            else:
                if right > 0:
                    right -= 1
                else:
                    return False
        return True


# This is a greedy solution using O(1) space, O(n) time (2 passes)
# from left to right, we always use free wildcards to become left open parentheses as needed
# from right to left, we always use free wildcards to become right open parentheses as needed


# there is actually a one pass solution shown below, where we match a pair in every loop iteration
class Solution:
    def checkValidString(self, s: str) -> bool:
        open_count = 0
        close_count = 0
        length = len(s) - 1

        # Traverse the string from both ends simultaneously
        for i in range(length + 1):
            # Count open parentheses or asterisks
            if s[i] == "(" or s[i] == "*":
                open_count += 1
            # otherwise in this case we need to match up a closing paren with an open one
            else:
                open_count -= 1

            # Count close parentheses or asterisks
            if s[length - i] == ")" or s[length - i] == "*":
                close_count += 1
            # otherwise in this case we need to match up an open paren with a closing one
            else:
                close_count -= 1

            # If at any point open count or close count goes negative, the string is invalid
            # we needed to match but didnt have the requisite symbol available
            if open_count < 0 or close_count < 0:
                return False

        # If open count and close count are both non-negative, the string is valid
        return True

from collections import deque


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        q = deque()
        n = len(s)
        res = ""
        last = {}
        for i in range(n - 1, -1, -1):
            c = s[i]
            if c not in last:
                last[c] = i
        for i in range(n):
            c = s[i]
            if c not in q:
                while q and c < q[-1] and i < last[q[-1]]:
                    q.pop()
                q.append(c)
        return "".join(list(q))


# what i was missing while doing this problem is tracking if this instance is the last occurence of a character or not.

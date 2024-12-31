from collections import Counter
import heapq


# since the counter only has up to 26 entries it's not too inefficient for the O(n) search to find the max key
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)
        res = []
        past = ("", 0)
        while len(counts) > 0:
            pastChar, pastCount = past
            current = max(counts)
            if pastCount > 0 and pastChar > current:
                removeCount = 1
            else:
                removeCount = min(counts[current], repeatLimit)
            res.append(current * removeCount)
            if pastCount > 0:
                counts[pastChar] = pastCount
            past = (current, counts[current] - removeCount)
            del counts[current]

        return "".join(res)


# we can do better using a hash map with the keys being the index in the alphabet.


from collections import Counter
import heapq


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        track = [(-ord(letter), count) for letter, count in Counter(s).items()]
        heapq.heapify(track)
        res = []

        while track:
            currentLetter, currentCount = heapq.heappop(track)
            removeCurrent = min(currentCount, repeatLimit)
            res.append(chr(-currentLetter) * removeCurrent)
            currentCount -= removeCurrent
            if track and currentCount > 0:
                nextLetter, nextCount = heapq.heappop(track)
                res.append(chr(-nextLetter))
                heapq.heappush(track, (currentLetter, currentCount))
                if nextCount > 1:
                    heapq.heappush(track, (nextLetter, nextCount - 1))
        return "".join(res)

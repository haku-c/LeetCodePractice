from collections import Counter

# import heapq


class Solution:
    def minimumLength(self, s: str) -> int:
        counts = Counter(s)
        res = 0
        for count in counts.values():
            if count & 1:
                res += 1
            else:
                res += 2
        return res
        # heap = []
        # for count in counts.values():
        #     heapq.heappush(heap, - count)
        # while heapq:
        #     # print(heap)
        #     top = heap[0]
        #     if -1*top >= 3:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, -(-1*top - 2))
        #     else:
        #         break
        # return -1*sum(heap)


# this question is a very simple math problem, but if you want to use actual cs techniques, you can technically use a max heap
# the idea is that odd counts of chars reduce down to 1, while even counts of chars reduce to 2
# you don't have to worry about the order of the characters since you can always pick the middle character if there are more than 3
# of that type remaining in the string.

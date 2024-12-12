import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        q = []
        heapq.heapify(q)
        for n in gifts:
            heapq.heappush(q, -n)
        for _ in range(k):
            top = heapq.heappop(q)
            heapq.heappush(q, -int((-top) ** 0.5))
        return -sum(q)


# perfect use for a heap since we need to poll the max value of the heap every step

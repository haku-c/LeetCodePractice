from collections import Counter


# this is the quickselect version
# the heap solution is using Counter elements, maintain a max heap of size k, then poll and return
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        self.qs = []
        for c in counts.keys():
            self.qs.append(c)

        # print(self.qs)
        def partition(left, right, counts):
            i = left
            pivot = counts[self.qs[right]]
            for j in range(left, right):
                if counts[self.qs[j]] <= pivot:
                    self.qs[j], self.qs[i] = self.qs[i], self.qs[j]
                    i += 1
            self.qs[i], self.qs[right] = self.qs[right], self.qs[i]
            return i

        def quickselect(k, left, right, counts):
            while left <= right:
                pivot = partition(left, right, counts)
                if pivot == k:
                    return pivot
                elif pivot > k:
                    right = pivot - 1
                else:
                    left = pivot + 1

        nth_smallest = len(self.qs) - k
        index = quickselect(nth_smallest, 0, len(self.qs) - 1, counts)
        # print(self.qs)
        # print(index)
        return self.qs[index:]

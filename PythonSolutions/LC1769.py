class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        pref = [int(boxes[0])] * n
        summation = 0
        for i in range(1, n):
            c = boxes[i]
            if c == "1":
                pref[i] = pref[i - 1] + 1
                summation += i
            else:
                pref[i] = pref[i - 1]
        res = [0] * n
        res[0] = summation
        for i in range(1, n):
            res[i] = res[i - 1] + pref[i - 1] - (pref[-1] - pref[i - 1])
        return res


# use a prefix sum to track, O(n) space and time

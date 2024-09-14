class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        pref = [0] * n
        pref[0] = arr[0]
        for i in range(1, n):
            pref[i] = pref[i - 1] ^ arr[i]
        res = [0] * (len(queries))
        for i in range(len(queries)):
            left, right = queries[i]
            if left == right:
                res[i] = arr[right]
            elif left == 0:
                res[i] = pref[right]
            else:
                res[i] = pref[right] ^ pref[left - 1]
        return res

class Solution:
    def countAndSay(self, n: int) -> str:
        # run length encoding.
        def rle(num):
            left = 0
            res = ""
            for i in range(1, len(num)):
                if num[i] != num[left]:
                    res += str(i - left) + num[left]
                    left = i
            res += str(len(num) - left) + num[left]
            return res

        seq = "1"
        for _ in range(n - 1):
            seq = rle(seq)
        return seq

class Solution:
    def maximumSwap(self, num: int) -> int:
        length = len(str(num))
        maxes = [0] * length
        curr = -1
        reverse = str(num)[::-1]

        def swap(a, b):
            number = list(str(num))
            temp = number[b]
            number[b] = number[a]
            number[a] = temp
            string = ""
            for i in number:
                string = "".join([string, i])
            return int(string)

        for i in range(length):
            c = int(reverse[i])
            if c > curr:
                curr = c
                ind = i
            maxes[i] = (curr, ind)
        for i in range(length):
            n, index = maxes[length - i - 1]
            if int(str(num)[i]) < n:
                res = swap(i, length - index - 1)
                return res
        return num

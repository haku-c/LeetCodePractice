class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        res = 0
        seq = defaultdict(list)
        lengthOneSeq = set()
        for n in arr:
            # always extend a fib seq if possible. Use a hashset to store all the sequences with f[-2] + f[-1] = n
            for priorSeq in seq[n]:
                length, last = priorSeq
                seq[last + n].append((length + 1, n))
                if length + 1 > res:
                    res = length + 1

            # use a set to quickly determine if we can form a fib sequence or not
            for num in lengthOneSeq:
                # use the inequalities to make sure we don't double count and we have a sorted order
                if n - num in lengthOneSeq and n - num > num:
                    seq[n + n - num].append((3, n))
                    res = max(3, res)
            # potentially start a new sequence with this number
            lengthOneSeq.add(n)
            # print(seq)

        return res


# proud of this solution

# use a hash set to store the sequences and and their lengths which we can add the current number to

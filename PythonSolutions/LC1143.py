class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        # if we don't select any characters from one string then the longest subseq is 0
        # therefore opt[0][:] and opt[:][0] should all be zero
        opt = [[0] * (n + 1) for _ in range(2)]
        for i in range(1, m + 1):
            c1 = text1[i - 1]
            for j in range(1, n + 1):
                c2 = text2[j - 1]
                # if the characters are the same, then the existing matching subsequence can expand by 1
                if c1 == c2:
                    opt[1][j] = opt[0][j - 1] + 1
                else:
                    # pick the max of the two previous if we can't expand the subsequence with the new characters
                    # the if else is faster than taking the max.
                    if opt[1][j - 1] > opt[0][j]:
                        opt[1][j] = opt[1][j - 1]
                    else:
                        opt[1][j] = opt[0][j]
            # copy the previous list over
            opt[0] = list(opt[1])
        # print(opt)
        return opt[1][n]


# similar to 1092
# opt[i][j] is length of longest subsequence including chars text1[:i] and text2[:j]
# here i save space by only using two length j arrays. Overwrite the previous row when we move on to the next character in text1

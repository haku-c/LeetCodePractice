class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1) + 1
        n = len(str2) + 1

        prior = [""] * (n)

        # for opt[0][j], str1 is empty and the optimal substring is just str2[:j]
        for j in range(1, n):
            prior[j] = str2[:j]

        for i in range(1, m):
            c1 = str1[i - 1]
            current = [""] * n
            # we always start the row assuming we have 0 characters from str2 and the first i characters from string 1
            current[0] = str1[:i]
            for j in range(1, n):
                c2 = str2[j - 1]
                # if the new characters are the same, then we only want to concatenate one instance of this new letter
                if c2 == c1:
                    current[j] = prior[j - 1] + c1
                # see the comment in the below code. The version here is a bit opaque since current is always refering to the
                # ith row in the opt table and prior always refers to the i-1 row
                elif len(prior[j]) > len(current[j - 1]):
                    current[j] = current[j - 1] + c2
                else:
                    current[j] = prior[j] + c1
            prior = current

        return current[n - 1]


# bottom up dp approach where we track the shortest commmon substring including certain characters in both strings
# opt[i][j] is the optimal substring for str1[0:i] and str2[0:j]
# do note we have an entire init loop where if it's say str1[0:0] the result is just str2[:j]
# then we have an extra column in the opt table to account if one string is empty.

# space saving version only tracks the 2 most recent rows in the table. (o.w MLE)

# here's the more readable solution
# class Solution:
#     def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
#         m = len(str1)
#         n = len(str2)
#         table = [[""] * (n + 1) for _ in range(m + 1)]
#         for i in range(1, m + 1):
#             table[i][0] = table[i - 1][0] + str1[i - 1]
#         for j in range(1, n + 1):
#             table[0][j] = table[0][j - 1] + str2[j - 1]

#         for i in range(1, m + 1):
#             c1 = str1[i - 1]
#             for j in range(1, n + 1):
#                 c2 = str2[j - 1]
#                 if c2 == c1:
#                     table[i][j] = table[i - 1][j - 1] + c1
# this is the tricky part, we want to set the current value (where we are on the ith row and jth column)
# if the characters differ, we have two options: either we tack on the character from str2 or the character from str1.
# since we have the best substring for str1[:i], str2[:j-1] and str1[:i-1], str2[:j] we can form a valid subsequence
# to include both the ith and jth character with either. So just pick the best!
#                 elif len(table[i - 1][j]) > len(table[i][j - 1]):
#                     table[i][j] = table[i][j - 1] + c2
#                 else:
#                     table[i][j] = table[i - 1][j] + c1

#         return table[m][n]

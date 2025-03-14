# class Solution:
#     def numberOfSubstrings(self, s: str) -> int:
#         # same approach as LC 3306
#         counts = [0,0,0]
#         start = 0
#         res = 0
#         for end in range(len(s)):
#             counts[ord(s[end]) - 97] += 1
#             while all(counts):
#                 res += len(s) - end
#                 counts[ord(s[start]) - 97] -= 1
#                 start += 1
#         return res


class Solution:
    def numberOfSubstrings(self, s):
        n = len(s)
        arr = [-1, -1, -1]
        cnt = 0
        for i in range(n):
            ch = s[i]
            arr[ord(ch) - ord("a")] = i
            cnt += 1 + min(arr)
        return cnt

    # we can make unique substrings based on the lowest position of the characters needed
    # instead of thinking of the window with a unique start, just fix the start to 0
    # instead keep expanding to the right
    # if we encountered all the values already, then the we need all characters from the right endpoint to the
    # lowest index amongst the character (to make a valid substring)
    # then all substrings including those chars can form more valid substrings with the chars to the left of
    # the lowest index amongst all characters

    # ex/
    # c a a a b b b c
    # when we encounter the next c, we need a b b b c to form a valid substring
    # anything to the left of the a can be added to form more unique substrings
    # a a b b b c, a a a b b b c, c a a a b b b c
    # notice how the additional substrings is 1 + the index of the rightmost occurence of a
    # we care about a in this case because a is the leftmost char in our base valid substring
    # it could be b or c depending on the string.

    # the base case has all counts set to -1 to indicate we can't form a valid substring at all.

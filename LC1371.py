class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        appearances = {}
        vowels = {"a": 16, "e": 8, "i": 4, "o": 2, "u": 1}
        current = 0
        appearances[0] = -1
        res = 0
        for index in range(len(s)):
            c = s[index]
            if c in vowels:
                current = current ^ vowels[c]
            if current not in appearances:
                appearances[current] = index
            else:
                res = max(res, index - appearances[current])
        return res


# I like this problem as the approach is not obvious at first glance.
# you can keep a running tally of the number of vowels using bits:
# have a bit mask of length 5 (each position represents if a vowel has an even or odd number encountered so far)
# in my version, i did aeiou so the leftmost bit is 'a', and the rightmost is 'u'
# so 00000 is all vowels have been encountered with an even number. If you encounter an 'e'
# then the position for 'e'should become a one, i.e 00000 -> 01000.
# if you encounter another 'e', then the running tally should once again become 00000, since you have seen 2 'e's (an even number of 'e's)
# notice if you encountered any odd number of only 'e's the bitmask is always 01000 and the bitmask is always 00000 if you encountered an even number of 'e's

# You can achieve this behavior by taking the xor of the running tally with 01000 when you encounter an 'e'
# (note 01000 is just 8 in decimal)
# similarly, you can xor with 10000 for encountering 'a', etc. etc.

# We can use this running tally to find the length of the subsequence by using this bit of logic:
# if the tally at index i is 01000 and the tally at index j is again 01000, then
# 1. there is an even amount of a,i,o,u between i and j
# 2. we encountered an odd number of 'e's at some index before i, so there are an even number of new 'e' between index i and j
# This implies there is an even number of vowels in the substring contained between i and j. So we can check if this substring is longer than our current max!

# so the rest of the solution is facilitating a quick retrieval of the first occurance of each different bitmask.
# We want the LONGEST substring, so we would want the leftmost and rightmost occurance of the bitmask during our iteration
# We can therefore stick the first occurance of every bitmask in a hashmap with the index of its occurance.

# Consider the following example:
# Note we start with appearances[0] = -1. This is for the edge case of if the string only has an even number of each individual vowel.
# beebelake
# index char bitmask
# 0     b    00000
# 1     e    01000 This is the first occurance of the bitmask 01000, so update appearances[01000] = 1
# 2     e    00000 We have seen 2 'e's which is an even number! Updating the result: index - appearances[00000] = 2 - (-1), res = 3
# 3     b    00000 Consonant. Update res again since we see 00000 again. index - appearances[00000] = 3 - (-1) = 4, res = 4
# 4     e    01000 Note the new qualifying substring "ebe" encountered which is represented by seeing 01000 again. No update to res since 3 < 4
# 5     l    01000 Note the qualifying substring "ebel". No update to res since 4 == 4
# 6     a    11000 New bitmask, update appearances[11000] = 6
# 7     k    11000 New qualifying substring of just "k". No update since index - appearances[11000] = 1 < 4
# 8     e    10000 appearances[10000] = 8.

#  The result becomes 4 with the substring "ebel" or "beeb"

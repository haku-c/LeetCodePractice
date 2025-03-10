# # binary search here instead of linear scan
# from collections import Counter


# def find(word):
#     left = 0
#     right = len(word)
#     while left <= right:
#         mid = left + (right - left) // 2
#         segment = word[mid : len(word)]
#         count = Counter(segment)
#         if (
#             "a" in count
#             and "e" in count
#             and "i" in count
#             and "o" in count
#             and "u" in count
#         ):
#             left = mid + 1
#         else:
#             right = mid - 1
#     print(left)
#     print(right)


class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        vowelCount = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        start = 0
        consonantCount = 0
        res = 0

        next_consonant = [0] * len(word)
        next_consonant_index = len(word)

        # this is the key trick: when we have a valid substring, all the vowels that come after this vowel make valid substrings that
        # count to result

        # zaeiouuuu k = 1, every u after the first creates a new valid substring: zaeiou, zaeiouu, zaeiouuu, zaeiouuuu
        # zaeiouuuuz k = 1 then we know we can expand up to the second z. Rather than loop, we precompute this with the next_consonant

        # if we encounter a vowel, we might also not need the leftmost-characters to be a valid vowel substring

        # azeiouauuz k = 1, when we get to the second a: azeioua is valid, zeioua is valid.
        # we need to count for those strings that don't use the left a

        #     Expanding: If we expand to another vowel, we know that this new substring is also valid. If the new character is a consonant, consonantCount exceeds k and we no longer have a valid substring. Thus, we can continue expanding our end boundary to find new substrings until we encounter a consonant. Precisely, if the next consonant is at index nextConsonantIndex, then we have a total of nextConsonantIndex - end new valid substrings. Instead of manually iterating to find the next consonant each time, we can precompute an array nextConsonant, where nextConsonant[i] stores the index of the next consonant after index i. With this, we can quickly determine how many new valid substrings can be formed from any valid window.
        #     Shrinking: We can find more valid substrings by shrinking our window until we no longer have a valid substring. For each new shrunken window, we can reapply the expanding logic discussed above, and create nextConsonant[end] - end new windows.

        for i in range(len(word) - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if not word[i] in vowels:
                next_consonant_index = i

        for i in range(len(word)):
            if word[i] in vowels:
                vowelCount[word[i]] += 1
            else:
                consonantCount += 1

            # if there are too many consonants, shrink the window until you get to the leftmost consonant
            while consonantCount > k and start <= i:
                if word[start] in vowels:
                    vowelCount[word[start]] -= 1
                else:
                    consonantCount -= 1
                start += 1

            # if the consonant count and the vowel count is correct, update
            # shrink the window until it is minumum size of a valid window
            while consonantCount == k and all(vowelCount.values()) and start <= i:
                res += next_consonant[i] - i
                if word[start] in vowels:
                    vowelCount[word[start]] -= 1
                else:
                    consonantCount -= 1
                start += 1

        return res


# there's an even cooler solution without the next cons structure:

# Intuition

# In the previous approach, we adjusted our sliding window by strictly following the 2 constraints:

#     A valid window must contain all vowels.
#     A valid window must contain exactly k consonants.

# The second requirement introduces more complexity to our sliding window solution, leading us to precompute a nextConsonant array to keep track of when the next consonant occurs for all indices in the string. To simplify the problem, let's relax this second constraint, so that valid substrings have at least k consonants instead.

# Let’s say we find a window (substring) that contains all vowels and exactly k consonants. What happens if we keep expanding the window to the right?

#     Adding more characters will never remove a vowel from the window.
#     It may add more consonants, but since we only need at least k, the window remains valid.

# This means that once we reach our first valid window (where end is the right boundary of the window), every substring that extends from this point onward is also valid. Instead of checking each one individually, we can instantly count them:

# New valid substrings=word.length−end

# After counting these substrings, we shrink the window from the left (start index) and repeat the process, making sure our window remains valid.

# Now, the question is how we can connect this relaxed version of the problem back to the original problem. Let's denote the solution to this relaxed problem with a given word and k as atLeastK(word, k). The key observation is the number of valid substrings (with exactly k consonants) is equal to atLeastK(word, k) - atLeastK(word, k + 1).

# (up to k) minus (up to k - 1) is exactly k

# With this problem reduction, we can simplify our sliding window approach and eliminate the need for an auxiliary data structure to keep track of occurrences of consonants.

# Source:
# https://codesignal.com/blog/interview-prep/example-codesignal-questions/

# Given an array a, your task is to output an array b of the same length by applying the following transformation:
# – For each i from 0 to a.length - 1 inclusive, b[i] = a[i - 1] + a[i] + a[i + 1]
# – If an element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, use 0 in its place
# – For instance, b[0] = 0 + a[0] + a[1]

from collections import defaultdict


def solution1(arr):
    n = len(arr)
    res = [0] * n
    for i in range(n):
        if i - 1 < 0:
            first = 0
        else:
            first = arr[i - 1]
        if i + 1 >= n:
            second = 0
        else:
            second = arr[i + 1]
        res[i] = first + arr[i] + second

    return res


# You are given two strings: pattern and source. The first string pattern contains only the symbols 0 and 1, and the second string source contains only lowercase English letters.

# Your task is to calculate the number of substrings of source that match pattern.

# We’ll say that a substring source[l..r] matches pattern if the following three conditions are met:
# – The pattern and substring are equal in length.
# – Where there is a 0 in the pattern, there is a vowel in the substring.
# – Where there is a 1 in the pattern, there is a consonant in the substring.

# Vowels are ‘a‘, ‘e‘, ‘i‘, ‘o‘, ‘u‘, and ‘y‘. All other letters are consonants.

# Example

# For pattern = "010" and source = "amazing", the output should be solution(pattern, source) = 2.
# – “010” matches source[0..2] = "ama". The pattern specifies “vowel, consonant, vowel”. “ama” matches this pattern: 0 matches a, 1 matches m, and 0 matches a.
# – “010” doesn’t match source[1..3] = "maz"
# – “010” matches source[2..4] = "azi"
# – “010” doesn’t match source[3..5] = "zin"
# – “010” doesn’t match source[4..6] = "ing"

# So, there are 2 matches. For a visual demonstration, see the example video.

# For pattern = "100" and source = "codesignal", the output should be solution(pattern, source) = 0.
# – There are no double vowels in the string "codesignal", so it’s not possible for any of its substrings to match this pattern.

# Guaranteed constraints:
# 1 ≤ source.length ≤ 103
# 1 ≤ pattern.length ≤ 103


def solution2(pattern, source):
    vowels = set(["a", "e", "i", "o", "u"])
    res = 0
    patternIndex = 0
    start = 0
    i = 0
    while i < len(source):
        c = source[i]
        if (pattern[patternIndex] == "0" and c in vowels) or (
            pattern[patternIndex] == "1" and c not in vowels
        ):
            patternIndex += 1
            i += 1
            if patternIndex >= len(pattern):
                res += 1
                patternIndex = 0
                start += 1
                i += start
        else:
            patternIndex = 0
            start += 1
            i = start
    return res


# the question is essentially tetris, trying to complete a row using a block
def solution3(field, figure):
    # process figure to get left-bottom most point
    def getCoords(figure):
        res = {}
        for row in range(2, -1, -1):
            for col in range(3):
                if figure[row][col]:
                    res[row].append(col)
        return res

    coords = getCoords(figure)
    width = len(field[0])
    height = len(field)
    maxCol = [-1] * width
    for i in range(height):
        for j in range(width):
            if field[i][j] and maxCol[j] != -1:
                maxCol[j] = i

    for col in range(width):
        connect = maxCol[col]
        for i in range(2, -1, -1):
            for j in coords[i]:
                pass


# this solution is a bit tricky, because you can double count the same number to form the desired sum

# i thought you could do some thing like 2,6 and 6,2 form 2 pairs in the count and divided by 2 we get the desired 1 pair in the result
# in the example, a single 2 gets used twice, and hence it would not form 2 pairs, throwing off the result if you built the dict beforehand and divided result by 2
# however, we can maintain the appropriate number if we iterate the array in order and only add to dict as we go
# then swapped pairs wont ever be formed.


def solution4(numbers):
    n = len(numbers)
    res = 0
    locations = defaultdict(int)

    for i in range(n):
        locations[numbers[i]] += 1
        for j in range(23):
            difference = 2**j - numbers[i]
            res += locations[difference]
    return res


if __name__ == "__main__":
    print(solution1([4, 0, 1, -2, 3]))
    print(solution1([4]))
    print(solution1([2, 4]))
    print(solution2("010", "amazing"))
    print(solution2("100", "codesignal"))
    print(solution4([-2, -1, 0, 1, 2]))

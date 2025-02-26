class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        oddCount = 0
        evenCount = 0
        res = 0
        for num in arr:
            if num % 2 == 1:
                evenCount, oddCount = oddCount, 1 + evenCount
            else:
                evenCount += 1
            res += oddCount % (10**9 + 7)
        return res % (10**9 + 7)


# same idea as 3247
# if we encounter an odd number, we can now create 1 more subarray of just that odd number,
# and one odd subarray for every even sum subarray previously encountered (even number + odd number is odd)
# the number of even subarrays

# if we encounter an even number, we can now create 1 more even subarray of just that number
# the number of odd subarrays remains the same since odd + even is odd.

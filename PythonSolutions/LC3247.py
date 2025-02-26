# Given an array nums, return the number of

# with an odd sum of elements.

# Since the answer may be very large, return it modulo 109 + 7.


class Solution:
    def subsequenceCount(self, arr: List[int]) -> int:
        oddCount = 0
        evenCount = 0
        for i in range(len(arr)):
            current = arr[i]
            if current % 2 == 1:
                evenCount, oddCount = (evenCount + oddCount) % (10**9 + 7), (
                    evenCount + oddCount + 1
                ) % (10**9 + 7)

            else:
                evenCount = (evenCount + evenCount + 1) % (10**9 + 7)
                oddCount = (oddCount + oddCount) % (10**9 + 7)

        return oddCount


# cases:
# if current is odd:
# we add 1 subsequence of just current number. We also gain a new odd subsequence for every single even sequence we had prior
# this is because we can concatenate the current number to an even subsequence to get an odd sum
# similarly, the number of even sequences increases by the number of odd sequences we had prior
# if current is even:
# the number of even sequences increases by 1 for just current. The number of even sequences also increases by the current number
# of even sequences (concatenate current to all prior even sequences)
# the number of odd sequences increases by the number of even sequences, since we can concatenate the current odd to any
# even sequence to get an odd sum sequence

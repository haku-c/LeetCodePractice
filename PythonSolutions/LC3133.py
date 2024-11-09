class Solution:
    def minEnd(self, n: int, x: int) -> int:
        res = []
        current = bin(x)[2:]
        fill = bin(n - 1)[2:]
        n = len(fill) - 1
        counter = 0
        for i in range(len(current) - 1, -1, -1):
            if current[i] == "0" and counter <= n:
                res.append(fill[n - counter])
                counter += 1
            else:
                res.append(current[i])
        string = "".join(res)[::-1]
        if counter <= n:
            string = "".join([fill[0 : n - counter + 1], string])
        return int(string, 2)


# the idea of this solution is you can construct the topmost number based on the number of "fixed" bits needed in the final solution.
# Since we need to AND all of the numbers in the sequence, we know all the bits set in X must be set in every number in the list.
# Then when we are generating numbers in the list under this constraint
# Every integer has a unique binary representation. We can use the binary form of x in our solution as follows:

# traverse from the right to left in the original binary representation of x. This is because we want the lowest possible result
# if we encounter a 1, then we know that value needs to stay as it is in the original (set bit).
# if we encounter a 0, substitute that 0 in the binary string to be the rightmost unused value in the binary representation of n - 1. Since this number is now used, move the counter so the next time we use the bit one position to the left. If we have used all the bits (n is very small) then keep whatever value was in the original binary form of x in that position.

# if n is large, we might not have enough "free" bits to change in the binary representation of x. Therefore, prepend the remaining unused bits of bin(n).

# note we use n-1 since x counts as the first value in the list. So if we need to find the answer for n = 2, we need
# to generate 1 extra number, if n = 3 we need to generate 2 extra numbers, etc.

# example:
# n = 3, x = 4
# binary of x is 100
# binary of 3 - 1 is 10
# fill from right to left:
# the two 00s become 10: 110 is the result. int('110', 2) becomes 6

# n = 2, x = 4
# binary of x is 100
# binary of 2 - 1 is 1
# fill from right to left we get 101 (note here we exhaust the fill bits)
# int('101', 2) is 5

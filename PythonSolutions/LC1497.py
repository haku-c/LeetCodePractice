class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counts = [0] * k
        for n in arr:
            counts[n % k] += 1
        for i in range(0, k):
            if i == 0 or i == k - i:
                if counts[i] % 2 != 0:
                    return False
            elif not counts[i] == counts[k - i]:
                return False
        return True


# the 2 catches here are if your mod operator can return negative values (it can't in python)
# and if the number n is already n mod k = zero, it can only be paired with other values also n mod k zero
# same idea if the number is n mod k = k / 2

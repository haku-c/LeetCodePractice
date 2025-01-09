class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[i + self.n] = nums[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        current = index + self.n
        self.tree[current] = val
        while current > 1:
            current //= 2
            self.tree[current] = self.tree[2 * current] + self.tree[2 * current + 1]

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n + 1
        s = 0
        while left < right:
            if left & 1:
                s += self.tree[left]
                left += 1
            if right & 1:
                right -= 1
                s += self.tree[right]
            left //= 2
            right //= 2
        return s


# the queries are inclusive of left and right in sumRange

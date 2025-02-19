class FenwickTree:
    def __init__(self, size, arr=None):
        self.tree = [0] * (size + 1)
        if arr is not None:
            for i in range(len(arr)):
                self.insert(i, arr[i])

    def sum(self, index):
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index

        return result

    # increment by 1 since BIT is 1 indexed
    def insert(self, index, value):
        index += 1
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def range_query(self, left, right):
        return self.sum(right) - self.sum(left - 1)


arr = [3, 2, -1, 6, 5, 4, -3]
bit = FenwickTree(7, arr)
print(bit.sum(3))
print(bit.range_query(2, 5))

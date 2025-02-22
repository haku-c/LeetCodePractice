class FenwickTree:
    def __init__(self, size, arr=None):
        self.tree = [0] * (size + 1)
        if arr is not None:
            for i in range(len(arr)):
                self.insert(i, arr[i])

    # this sum function is inclusive of the last element and 0 based
    def sum(self, index):
        index += 1
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

freq = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
bit2 = FenwickTree(12, freq)
print("Sum of elements in arr[0..5] is " + str(bit2.sum(5)))
bit2.insert(3, 6)

print("Sum of elements in arr[0..5]" + " after update is " + str(bit2.sum(5)))

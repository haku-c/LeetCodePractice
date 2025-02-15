class ProductOfNumbers:

    def __init__(self):
        self.table = {}
        self.pref = 1

    def add(self, num: int) -> None:
        if num != 0:
            n = len(self.table)
            self.pref *= num
            self.table[n] = self.pref
        else:
            self.table.clear()
            self.pref = 1

    def getProduct(self, k: int) -> int:
        if k > len(self.table):
            return 0
        if k == len(self.table):
            return self.pref
        return int(self.pref / self.table[(len(self.table) - 1 - k)])


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

# you can use a list for the table since the keys are always just list index

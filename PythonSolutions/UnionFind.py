class UnionFind:
    def __init__(self, size):
        self.parents = list(range(0, size))
        self.sizes = [1] * size

    def find(self, index):
        if index == self.parents[index]:
            return self.parents[index]
        else:
            return self.find(self.parents[index])

    def union(self, left, right):
        leftRep = self.find(left)
        rightRep = self.find(right)
        if leftRep == rightRep:
            return

        leftSize = self.sizes[leftRep]
        rightSize = self.sizes[rightRep]

        if leftSize >= rightSize:
            self.parents[rightRep] = leftRep
            self.sizes[leftRep] += self.sizes[rightRep]
        else:
            self.parents[leftRep] = rightRep
            self.sizes[rightRep] += self.sizes[leftRep]

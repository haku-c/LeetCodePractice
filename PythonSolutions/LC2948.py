class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.sizes = [1] * n

    def union(self, x, y):
        repx = self.find(x)
        repy = self.find(y)
        sx = self.sizes[repx]
        sy = self.sizes[repy]
        if sx >= sy:
            self.sizes[repx] += sy
            self.parents[repy] = repx
        else:
            self.sizes[repy] += sx
            self.parents[repx] = repy

    def find(self, x):
        if self.parents[x] == x:
            return x
        return self.find(self.parents[x])


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        uf = UnionFind(n)
        starts = {}
        sort_index = [i for i, x in sorted(enumerate(nums), key=lambda x: x[1])]
        for i in range(n):
            if i > 0 and abs(nums[sort_index[i - 1]] - nums[sort_index[i]]) <= limit:
                # print("union" + str(sort_index[i-1]) + " " + str(sort_index[i]))
                uf.union(sort_index[i - 1], sort_index[i])
            else:
                starts[sort_index[i]] = i, 0
        res = [0] * n
        for i in range(n):
            rep = uf.find(i)
            ind, offset = starts[rep]
            res[i] = nums[sort_index[ind + offset]]
            starts[rep] = ind, offset + 1
        return res


# this solution is correct, but it is needlessly complicated and a headache to understand

# faster and simpler solution below: (uses the same idea of sorting to find the appropriate groups)


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        starts = {}
        groups = [0] * n
        sort_index = [i for i, x in sorted(enumerate(nums), key=lambda x: x[1])]
        group = 0
        starts[0] = 0
        for i in range(1, n):
            if abs(nums[sort_index[i - 1]] - nums[sort_index[i]]) > limit:
                group += 1
                starts[group] = i
            groups[sort_index[i]] = group

        res = [0] * n
        for i in range(n):
            rep = groups[i]
            ind = starts[rep]
            res[i] = nums[sort_index[ind]]
            starts[rep] = ind + 1
        return res

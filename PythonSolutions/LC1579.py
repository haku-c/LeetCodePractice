# unionset data structure with path shortening and a heuristic to keep the size of trees to be logn
class UnionSet:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.sizes = [1] * (n + 1)

    # if we have not reached the root of this group, continue recursing.
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        xsize = self.sizes[xrep]
        ysize = self.sizes[yrep]
        if xrep == yrep:
            return
        if ysize > xsize:
            self.parent[xrep] = yrep
            self.sizes[yrep] += xsize
        else:
            self.parent[yrep] = xrep
            self.sizes[xrep] += ysize


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # if one of the nodes is not in the same group as the other, make them part of the same group by union
        def extend(unionSet: UnionSet, u, v):
            if unionSet.find(v) != unionSet.find(u):
                unionSet.union(u, v)
                return 1
            return 0

        # since all nodes are in the same group when we have built a spanning graph, we know the representative for any
        # one node will be the same across them all. The size of the tree for this should consist of every node (be n)
        def finished(unionSet: UnionSet, n):
            return unionSet.sizes[unionSet.find(1)] == n

        # sort the edges to process type 3 edges first so we can early stop if we can connect the graph fully with type 3 edges.
        edges.sort(key=lambda x: x[0], reverse=True)
        AliceSets = UnionSet(n)
        BobSets = UnionSet(n)
        totalcount = 0
        for typeEdge, u, v in edges:
            if typeEdge == 3:
                if extend(AliceSets, u, v) and extend(BobSets, u, v):
                    totalcount += 1
                if finished(AliceSets, n):
                    return len(edges) - totalcount
            elif typeEdge == 1:
                totalcount += extend(AliceSets, u, v)
                if finished(AliceSets, n):
                    pass
            else:
                totalcount += extend(BobSets, u, v)
                if finished(BobSets, n):
                    pass
        # if either Alice or Bob cannot traverse return -1
        if not finished(AliceSets, n) or not finished(BobSets, n):
            return -1
        return len(edges) - totalcount

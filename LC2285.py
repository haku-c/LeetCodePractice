def maximumImportance(self, n, roads):
    """
    :type n: int
    :type roads: List[List[int]]
    :rtype: int
    """
    # count[i] shows how many roads is connected to city i
    # my solution uses sorting when you don't have to
    count = [0 for i in range(n)]
    for a, b in roads:
        count[a] += 1
        count[b] += 1
    index = [*range(0, n)]
    index = [x for _, x in sorted(zip(count, index))]
    assignments = [0 for i in range(n)]
    for i in range(n):
        assignments[index[i]] = i + 1
    s = 0
    for a, b in roads:
        s += assignments[a] + assignments[b]
    return s


# better:
# count = [0 for i in range(n)]
# for a, b in roads:
#   count[a] += 1
#   count[b] += 1
# count.sort()
# for index in range(1,n+1):
#     s += count[index-1] * index

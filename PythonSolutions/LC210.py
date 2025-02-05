from collections import defaultdict, deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        # build the graph and store indegree counts
        for following, prior in prerequisites:
            indegrees[following] += 1
            graph[prior].append(following)
        q = deque()
        # initialize the queue with all courses that start a prereq chain
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        res = []
        while q:
            currentCourse = q.pop()
            res.append(currentCourse)
            for following in graph[currentCourse]:
                indegrees[following] -= 1
                if indegrees[following] == 0:
                    q.append(following)

        return res if len(res) == numCourses else []


# use khan's (bfs) to get topological sorting.

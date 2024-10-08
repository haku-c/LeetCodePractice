class Solution:
    def createSpiral(self, n):

        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]]
        # left edge, bottom edge, right edge, top edge
        edges = [0, n - 1, n - 1, 2]
        res = [[" "] * n for i in range(n)]
        self.repeat = 0

        # def opposite(direction):
        #     if direction == 0:
        #         return 2
        #     elif direction == 1:
        #         return 3
        #     elif direction == 2:
        #         return 0
        #     else:
        #         return 1

        # def check(x, y, direction):
        #     if x < 0 or x >= n or y < 0 or y >= n:
        #         self.repeat += 1
        #         return False
        #     for i in range(4):
        #         if i == opposite(direction):
        #             continue
        #         deltaX, deltaY = directions[direction]
        #         if (
        #             x + deltaX < 0
        #             or x + deltaX >= n
        #             or y + deltaY < 0
        #             or y + deltaY >= n
        #         ):
        #             continue
        #         elif res[x + deltaX][y + deltaY] == "#":
        #             self.repeat += 1
        #             return False
        #     self.repeat = 0
        #     return True

        x = 0
        currentDir = 0
        y = n - 1
        for _ in range(n * n):
            deltaX, deltaY = directions[currentDir]
            res[x][y] = "#"
            x += deltaX
            y += deltaY
            if (edges[2] - edges[0]) < -1 or (edges[1] - edges[3]) < -1:
                print(edges)
                break
            if currentDir == 0 and y == edges[currentDir]:
                edges[currentDir] += 2
                currentDir = (currentDir + 1) % 4
            elif currentDir == 1 and x == edges[currentDir]:
                edges[currentDir] -= 2
                currentDir = (currentDir + 1) % 4
            elif currentDir == 2 and y == edges[currentDir]:
                edges[currentDir] -= 2
                currentDir = (currentDir + 1) % 4
            elif currentDir == 3 and x == edges[currentDir]:
                edges[currentDir] += 2
                currentDir = (currentDir + 1) % 4
        # for i in range(n * n):
        #     deltaX, deltaY = directions[currentDir]
        #     print(x)
        #     print(y)
        #     res[x][y] = "#"
        #     x += deltaX
        #     y += deltaY
        #     if not check(x, y, currentDir):
        #         if self.repeat == 4:
        #             break
        #         currentDir = (currentDir + 1) % 4
        for row in res:
            print("".join(row))


test = Solution()
test.createSpiral(30)

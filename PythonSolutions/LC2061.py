class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        m = len(room)
        n = len(room[0])
        visited = [[-1] * n for _ in range(m)]
        res = 1
        currentRow, currentCol, direction, stuck = 0, 0, 0, 0
        visited[0][0] = 0
        while True:
            deltaRow, deltaCol = directions[direction]
            newRow, newCol = currentRow + deltaRow, currentCol + deltaCol
            # if we loop or we are boxed in, exit
            if (
                0 <= newRow < m
                and 0 <= newCol < n
                and visited[newRow][newCol] == direction
            ) or stuck == 4:
                break
            # if we are not boxed in, move in that direction. increment the result if we have not been to that location
            elif 0 <= newRow < m and 0 <= newCol < n and room[newRow][newCol] == 0:
                currentRow, currentCol = newRow, newCol
                stuck = 0
                if visited[newRow][newCol] == -1:
                    visited[newRow][newCol] = direction
                    res += 1
            # if we run into an obstacle or outside the grid, change directions. Track how many times we have changed directions at this location
            else:
                direction = (direction + 1) % 4
                stuck += 1

        return res


# the key insight here is we need to track both the direction we are going at a certain location and if we have already been there before
# it's not enough to check if we have already been to that location only.

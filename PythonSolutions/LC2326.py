# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * n for i in range(m)]
        current = head
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        currentDirection = 0
        x = 0
        y = 0
        xDelta, yDelta = directions[currentDirection]
        while current:
            res[x][y] = current.val
            tempX = x + xDelta
            tempY = y + yDelta
            if (
                tempX < 0
                or tempX == m
                or tempY < 0
                or tempY == n
                or res[tempX][tempY] != -1
            ):
                currentDirection = (currentDirection + 1) % 4
                xDelta, yDelta = directions[currentDirection]
                x += xDelta
                y += yDelta
            else:
                x = tempX
                y = tempY
            current = current.next
        return res

import pprint


def findPaths(m, n, maxMove, startRow, startColumn):
    arr = [[[-1 for i in range(m)] for j in range(n)] for k in range(maxMove + 1)]
    pprint(arr)
    return recurse(arr, m, n, startRow, startColumn, maxMove)


def recurse(arr, m, n, startRow, startColumn, moves):
    # we got outside from the previous move
    if startRow < 0 or startColumn < 0 or startRow >= m or startColumn >= n:
        return 1
    # we ran out of moves
    if moves == 0:
        return 0
    # optimization to not repeat work
    if arr[moves][startColumn][startRow] >= 0:
        return arr[moves][startColumn][startRow]
    # recursive step where we step in every direction
    arr[moves][startColumn][startRow] = (
        recurse(arr, m, n, startRow + 1, startColumn, moves - 1)
        + recurse(
            arr,
            m,
            n,
            startRow - 1,
            startColumn,
            moves - 1,
        )
        + recurse(arr, m, n, startRow, startColumn + 1, moves - 1)
        + recurse(arr, m, n, startRow, startColumn - 1, moves - 1)
    )
    return arr[moves][startColumn][startRow]

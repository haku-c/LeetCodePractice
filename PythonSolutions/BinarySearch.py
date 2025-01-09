def searchLeft(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        current = start + ((end - start) // 2)
        if arr[current] < target:
            start = current + 1
        else:
            end = current - 1
    return start


def searchRight(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        current = start + ((end - start) // 2)
        if arr[current] <= target:
            start = current + 1
        else:
            end = current - 1
    return start

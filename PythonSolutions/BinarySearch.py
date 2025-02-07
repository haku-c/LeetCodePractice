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
    return end


def findLeftMostIndex(nums, target):
    left = 0
    right = nums.length - 1
    leftMostIndex = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            leftMostIndex = mid
            right = mid - 1
    return leftMostIndex


def findRightMostIndex(nums, target):
    left = 0
    right = len(nums) - 1
    rightMostIndex = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            rightMostIndex = mid
            left = mid + 1
    return rightMostIndex

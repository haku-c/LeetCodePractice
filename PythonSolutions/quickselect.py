def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i


def quickselect(nums, k, left, right):
    while left <= right:
        pivot = partition(nums, left, right)
        if pivot == k:
            return nums[pivot]
        elif pivot > k:
            right = pivot - 1
        else:
            left = pivot + 1
    return nums[left]


# if the problem is to find the kth largest number, pass nth_smallest.
# this is because quickselect looks for the smallest kth integer by default


def findk(arr, k):
    # nth_smallest = len(arr) - k
    # this quickselect is 0 based, so k = 0 returns the smallest integer
    # if you want k = 1 to be the smallest integer, pass k - 1
    return quickselect(arr, k, 0, len(arr) - 1)


# this "vanilla" version of quickselect performs poorly when there are many duplicate elements.
# in the general case this is fine, but contrived inputs can give O(n^2), so make sure to also have a heaps solution handy

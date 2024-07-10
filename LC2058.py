def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
    res = [-1, -1]
    current = head.next
    prevCritIndex = firstCritIndex = -1
    isGreater = current.val > head.val
    isLess = current.val < head.val
    index = 1
    while current.next is not None:
        if (isGreater and current.val > current.next.val) or (
            isLess and current.val < current.next.val
        ):
            # if this is the first critical value, update the previous pointers but don't update result
            if prevCritIndex == -1:
                firstCritIndex = index
            else:
                res[0] = (
                    index - prevCritIndex
                    if res[0] == -1
                    else min(res[0], index - prevCritIndex)
                )
            prevCritIndex = index
        isGreater = current.next.val > current.val
        isLess = current.next.val < current.val
        index += 1
        current = current.next
    if res[0] != -1:
        res[1] = max(res[1], prevCritIndex - firstCritIndex)
    return res


# this solution is a bit more optimized if you don't reassign the values in
# the array every time (for the max values)
# You can also use 3 pointers instead of a boolean

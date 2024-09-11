# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        n = 0
        current = head
        res = [None] * k
        while current:
            n += 1
            current = current.next

        if n < k:
            current = head
            for i in range(n):
                res[i] = current
                nxt = current.next
                current.next = None
                current = nxt
            return res

        target = n // k
        remaining = n - (target * k)
        current = head
        for i in range(k):
            size = target + 1 if i < remaining else target
            res[i] = current
            for _ in range(size - 1):
                current = current.next

            nxt = current.next
            current.next = None
            current = nxt

        return res

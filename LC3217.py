# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        first = None
        current = head
        forbidden = set(nums)
        # res becomes the first node where the current value is not in forbidden
        while current.val in forbidden:
            current = current.next
        res = current
        pter = current
        # move the list up one so pter points to the last valid node and current is unexplored
        current = current.next
        while current is not None:
            # skip all nodes where the current value is forbidden. After this loop, the current node should have a valid value
            while current is not None and current.val in forbidden:
                current = current.next
            pter.next = current
            pter = current
            if current is not None:
                current = current.next
                pter.next = None
        return res


# cleaner solution below:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = head
        forbidden = set(nums)
        # res becomes the first node where the current value is not in forbidden
        while current.val in forbidden:
            current = current.next
        res = current
        # change the next pointer here.
        while current.next:
            if current.next.val in forbidden:
                current.next = current.next.next
            else:
                current = current.next

        return res

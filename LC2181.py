def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # def sumNodes(sum, node, past, start):
    #     if node is None:
    #         return start
    #     if node.val != 0:
    #         sum += node.val
    #         return sumNodes(sum, node.next, past, start)
    #     else:
    #         # if this node is the second 0 in the linked list, this is the result
    #         node.val = sum
    #         if start is None:
    #             start = node
    #         else:
    #             past.next = node
    #         return sumNodes(0, node.next, node, start)
    # return sumNodes(0, head.next, None, None)
    past = None
    current = head.next
    sum = 0
    flag = False
    while current:
        if current.val != 0:
            sum += current.val
        else:
            current.val = sum
            if not flag:
                head = current
                flag = True
            else:
                past.next = current
            past = current
            sum = 0
        current = current.next
    return head


# using a while loop saves space since you dont copy variables onto the stack
# you also don't have to create a new dummy variable for the new root (replace the head)
# sacrifice readability for speed?

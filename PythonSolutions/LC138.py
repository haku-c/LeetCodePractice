"""
# Definition for a Node.
"""


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # index all the nodes first, creating node copies in one pass
        # in second pass of the completed copy, add the random pointers based on the index
        # need 2 dictionaries to track indexes
        newHead = Node(head.val)
        mapping = {id(head): newHead}
        newCurr = newHead
        currOld = head.next
        while currOld != None:
            newNode = Node(currOld.val)
            newCurr.next = newNode
            # map this node to the newNode copy of it
            mapping[id(currOld)] = newNode
            # iterate
            currOld = currOld.next
            newCurr = newCurr.next

        currOld = head
        newCurr = newHead
        while currOld != None and newCurr != None:
            if currOld.random != None:
                newCurr.random = mapping[id(currOld.random)]
            currOld = currOld.next
            newCurr = newCurr.next

        return newHead

    # forgot to iterate the newCurrent and was failing on test cases greater than length 2

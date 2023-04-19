public class LC24 {

    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null)
            return head;

        // 3 pointers and recursion since you need to restitch the list.
        ListNode temp = head.next.next;
        ListNode second = head;
        ListNode first = head.next;

        head = first;
        head.next = second;
        head.next.next = swapPairs(temp);

        return head;
    }
}

// 1 2 3 4 5 6
// temp is 3, first is 2 , second is 1
// easy swap 2 and 1 and then recurse on the third in the list.

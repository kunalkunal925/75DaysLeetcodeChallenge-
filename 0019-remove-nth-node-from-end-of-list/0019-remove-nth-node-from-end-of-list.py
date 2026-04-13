class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        first = dummy
        second = dummy
        
        for _ in range(n + 1):
            first = first.next
            
        while first:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        
        return dummy.next
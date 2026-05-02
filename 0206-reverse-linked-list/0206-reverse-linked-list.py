class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Agle node ko save karein
            curr.next = prev       # Pointer ko reverse karein
            prev = curr            # prev ko aage badhayein
            curr = next_node       # curr ko aage badhayein
            
        return prev
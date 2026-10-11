class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Dummy head to help build the result list easily
        ListNode dummyHead = new ListNode(0);
        ListNode current = dummyHead;
        int carry = 0;
        
        // Loop while there is still data to process in the lists or a carry left over
        while (l1 != null || l2 != null || carry != 0) {
            // Get the value from the current node, or zero if the list has ended
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;
            
            // Add the two digits and the carry from the last step
            int sum = x + y + carry;
            
            // Calculate the new carry (either 0 or 1)
            carry = sum / 10;
            
            // Create a new node with the last digit of the sum and link it
            current.next = new ListNode(sum % 10);
            current = current.next;
            
            // Move to the next nodes in the input lists if they exist
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }
        
        // Return the final list starting after the dummy head
        return dummyHead.next;
    }
}
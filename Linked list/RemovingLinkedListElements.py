# 203. Remove Linked List Elements
# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val==val:
            head=head.next
        
        if not head:
            return head


        current=head
        while current:
            if current.next and current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next

        return head
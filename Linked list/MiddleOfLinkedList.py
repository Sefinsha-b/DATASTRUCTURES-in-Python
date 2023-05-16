# 876. Middle of the Linked List

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Tortoise,hair=head,head
        while hair and hair.next:
            Tortoise=Tortoise.next
            hair=hair.next.next
        return Tortoise
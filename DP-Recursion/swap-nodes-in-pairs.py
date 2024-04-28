# lc 24
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        n1, n2, n3 = head, head.next, head.next.next

        n2.next = n1
        n1.next = self.swapPairs(n3)
        return n2
        
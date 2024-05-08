# lc 234
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time O(n), Space O(1)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        mid = self.find_mid(head)
        sec_head = self.reverse(mid.next)

        while sec_head:
            if sec_head.val != head.val:
                return False
            sec_head = sec_head.next
            head = head.next
        return True

    def find_mid(self, head: ListNode) -> ListNode:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
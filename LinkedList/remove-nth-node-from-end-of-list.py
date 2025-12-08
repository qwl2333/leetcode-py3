from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #  cornor case  head: [1], n = 1 expected None
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        
        slow, fast = head, head
        dummy = ListNode(-1)
        pre = dummy
        pre.next = head
        while fast:
            if n == 0:
                slow = slow.next
                pre = pre.next
            else:
                n -= 1
            fast = fast.next
        
        pre.next = slow.next

        return dummy.next # 为什么不直接返回原来的head, 因为head可能已经被删除了
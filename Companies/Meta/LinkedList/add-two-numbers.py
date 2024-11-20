# lc 2
# 和 lc 415 Add Strings 类似
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        new_head = dummy

        carry_bit = 0
        while l1 or l2:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            
            new_val = (v1 + v2 + carry_bit) % 10
            carry_bit = (v1 + v2 + carry_bit) // 10
            new_node = ListNode(new_val)
            new_head.next = new_node
            new_head = new_node     
        
        if carry_bit == 1:
            new_node = ListNode(1)
            new_head.next = new_node
        
        return dummy.next

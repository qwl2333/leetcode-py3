# lc 160 和 lc 1650 lcaiii 类似
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    '''
    For those who struggle: let's split the both paths into s1 = s1_diff + common and s2 = s2_diff + common. 
    The common part is the part which is, well, common for both of the paths. 
    On the second iteration the first pointer will go through s1_diff + common + s2_diff. 
    The second pointer will go through s2_diff + common + s1_diff. After they go through those paths, they will meet. 
    If there is no common part, then the both pointers will be null
    '''
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
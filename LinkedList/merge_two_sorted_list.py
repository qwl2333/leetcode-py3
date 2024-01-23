# lc 21
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        cur = prehead
        while list1 != None and list2 != None:
            if list1.val > list2.val:
                cur.next = list2
                cur = list2
                list2 = list2.next
            else:
                cur.next = list1
                cur = list1
                list1 = list1.next
        
        if list1 == None:
            cur.next = list2
        else:
            cur.next = list1

        return prehead.next

a = Solution()
# Create nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

new_head = a.mergeTwoLists(node1, node4)
while new_head:
    print(new_head.val)
    new_head = new_head.next
        

            


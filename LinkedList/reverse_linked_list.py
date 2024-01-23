from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Iterative solution
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        prev = None
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        return prev
    
    # Recursive solution
    def reverseListRec(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.reverseListHelper()
    
    # 假如输入是 1->2->3->4->5，中间某一个时间点
    # prev 1<-2<-3 head 4->5
    # 这代表着 prev是已经reverse过的list的头部，head是还没reverse的list的头部    
    def reverseListHelper(self, prev: Optional[ListNode], head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverseListHelper(head, next)


s = Solution()
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

new_head = s.reverseList(node1)
while new_head:
    print(new_head.val)
    new_head = new_head.next

        
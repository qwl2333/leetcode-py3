# lc 369 和 lc 66 类似，判断加1之后有没有到10，到了10变为0
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # TC: O(N) SC: O(1)
    # 在头节点前加一个 sentinel (哨兵) 节点，防止 [9, 9, 9] 这种情况。
    # 找到链表中 最后一个不是 9 的节点。
    # 将这个节点的值加 1。
    # 将这个节点之后的所有节点全部变为 0。
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy

        # 1. 找到最后一个不是 9 的节点
        cur = head
        while cur:
            if cur.val != 9:
                not_nine = cur
            cur = cur.next

        # 2. 最后一个非 9 节点加 1
        not_nine.val += 1

        # 3. 将其之后的所有节点设为 0
        cur = not_nine.next
        while cur:
            cur.val = 0
            cur = cur.next
        
        return dummy if dummy.val == 1 else head
    
    # TC: O(N) SC: O(1)
    # 这是最符合直觉的方案：翻转链表，按数组加法处理，最后再翻转回来。
    def plusOne2(self, head: ListNode) -> ListNode:
        # 辅助函数：翻转链表
        def reverse(head: ListNode):
            prev = None
            cur = head
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        # 1. 翻转
        new_head = reverse(head) # 原来的head留着,之后有用

        cur = new_head
        # 2. 加1
        while cur:
            if cur.val < 9:
                cur.val += 1
                break
            cur.val = 0
            cur = cur.next
        # 如果到头了还是0，说明是9->9->9 的情况
        if head.val == 0:
            head.next = ListNode(1) # 原来的head现在就是队尾了
        
        # 3. 翻转回来
        return reverse(new_head) 
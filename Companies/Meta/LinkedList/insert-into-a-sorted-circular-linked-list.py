# lc 708
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    # Time O(n), space O(1) n - length of linked list
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        if not head:
            new_node.next = new_node
            return new_node

        cur = head
        tail = head
        back_to_head = False
        while not back_to_head:
            if cur.val <= insertVal <= cur.next.val:
                next = cur.next
                cur.next = new_node
                new_node.next = next
                return head
            if cur.val > cur.next.val: # tail一定是严格大于右边的，除非所有点都是一样大小，那tail就永远在head了，此时插入哪都行
                tail = cur
            cur = cur.next
            if cur == head:
                back_to_head = True
        # 要么所有点都比insertVal大（cur.val <= insertVal 满足不了）
        # 要么所有点都比insertVal小 （cur.next.val >= insertVal 满足不了）
        # 但是都可以 append the new_node after the tail，就是new_node要么是新的头要么是新的尾
        # 所以在遍历的时候要找tail
        next = tail.next
        tail.next = new_node
        new_node.next = next
        return head

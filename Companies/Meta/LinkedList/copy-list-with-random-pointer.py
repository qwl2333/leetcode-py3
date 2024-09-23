# lc 138
# https://leetcode.com/problems/copy-list-with-random-pointer/solutions/4003262/97-92-hash-table-linked-list/
# 此题还有t O(n), s O(1)的解法, 就是把new_node加到 old_node和old_node.next之间
# 参考link里面的Code #2 Interweaving Nodes
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    # time O(2n), space O(n) - n is number of nodes in the list
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}
        cur = head
        while cur:
            if cur not in old_to_new:
                old_to_new[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            if cur.next:
                old_to_new[cur].next = old_to_new[cur.next]
            if cur.random:
                old_to_new[cur].random = old_to_new[cur.random]
            cur = cur.next
        
        return old_to_new[head]
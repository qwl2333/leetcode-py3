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
    # 节省一个map的写法
    # time O(3n), space O(1) 如果不算新node - n is number of nodes in the list
    def copyRandomList2(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1) Interleave: a -> a' -> b -> b' ...
        cur = head
        while cur:
            clone = Node(cur.val)
            next_node = cur.next
            cur.next = clone
            clone.next = next_node
            cur = next_node

        # 给新node的random连起来必须和detach步骤分开做，2，3不能合在一起
        # Originals: A -> B -> C
        # Clones interleaved: A -> A' -> B -> B' -> C -> C'
        # Suppose C.random = A.
        # If you already detached A when you reach C, then A.next is B (not A').
        # Your code sets C'.random = A.next = B → wrong.

        # 2) Set clone.random while still interleaved
        cur = head
        while cur:
            clone = cur.next
            if cur.random:
                clone.random = cur.random.next
            cur = clone.next  # move to next original

        # 3) Detach
        cur = head
        new_head = head.next
        while cur:
            clone = cur.next
            cur.next = clone.next            # restore original
            if clone.next:
                clone.next = clone.next.next # link clones
            cur = cur.next

        return new_head

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
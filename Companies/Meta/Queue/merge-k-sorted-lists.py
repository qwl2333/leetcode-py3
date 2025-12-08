# lc 23
import heapq
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # edge case 要考虑 lists = [] 和 lists = [None]
    # merge k sorted lists using min heap
    # time O(n*logk)   space O(k)   k: number of lists that need to be merged, n: total number of nodes of all lists
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap, res = [], ListNode()
        for i, list in enumerate(lists):
            if list:
                heapq.heappush(heap, (list.val, i, list)) # 加i进来是in case list.val一样，因为只放k个list,
                                                          # 所以保证了i一定不一样, 不会出现i也一样的情况
                                                          # 也可以id(list)来代替i
                                                          # 所以heap的size不会超过k

        cur = res
        while heap:
            _, i, list = heapq.heappop(heap)
            if list.next:
                heapq.heappush(heap, (list.next.val, i, list.next))

            cur.next, cur = list, list

        return res.next

    # Brute force
    # time O(k^2n) k: number of lists that need to be merged, n: average length of each list
    # space O(m) m - number of nodes in the lists, imagine merge 2 list in the last time
    # one is very long close to m, the other might only have 2 or 3, so the stack we need in the worst case is close to m
    def mergeKLists2(self, lists):
        if len(lists) == 0:
            return None
        merged = None
        for head in lists:
            merged = self.mergeTwoSortedLists(merged, head)
        return merged

    def mergeTwoSortedLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val < l2.val:
            l1.next = self.mergeTwoSortedLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoSortedLists(l1, l2.next)
            return l2
    
    # Merge sort divide and conquer
    # k : number of lists,  n: number of nodes in all k list
    # time O(n*logk) -  (height of stack)logk * n      
    # space O(logk) logk is the height of the binary tree. The space for stack we use
    def mergeKListsMergeSort(self, lists):
        if not lists:
            return None
        return self.mergeKListsRecursive(lists, 0, len(lists) - 1)

    def mergeKListsRecursive(self, lists, start, end):
        if start == end:
            return lists[start]

        mid = (start + end) // 2
        lower = self.mergeKListsRecursive(lists, start, mid)
        upper = self.mergeKListsRecursive(lists, mid + 1, end)

        return self.mergeTwoSortedLists(lower, upper)
    
    # Merge sort iterative
    # k : number of lists,  n: number of nodes in all k list
    # time O(n*logk) -  (height of stack)logk * n      
    # space O(1)
    def mergeKListsIterative(self, lists: list['ListNode']) -> 'ListNode':
        if not lists:
            return None
        
        amount = len(lists)
        interval = 1 
        
        # ----------------------------------------------------
        # 算法流程示例（迭代分治合并）
        # 假设初始 lists 有 4 个链表：[L0, L1, L2, L3]
        # ----------------------------------------------------
        
        # 核心迭代循环：interval 决定了每次合并的步长
        while interval < amount:
            
            # 遍历并执行两两合并。i 从 0 开始，步长为 interval * 2
            for i in range(0, amount - interval, interval * 2):
                
                # 当前正在合并的链表对是：lists[i] 和 lists[i + interval]
                
                # 使用 mergeTwoSortedLists 辅助函数进行合并，并将结果存回 lists[i]
                lists[i] = self.mergeTwoSortedLists(lists[i], lists[i + interval])
                
            # --- 示例追踪 ---
            # 初始: amount = 4, interval = 1
            # 
            # 第 1 轮 (interval = 1):
            # 1. i=0: 合并 (L0, L1)，结果存回 L0。
            # 2. i=2: 合并 (L2, L3)，结果存回 L2。
            # 此时数组的有效链表是 [(L0+L1), L1, (L2+L3), L3]
            # interval 变为 2。
            
            # 第 2 轮 (interval = 2):
            # 1. i=0: 合并 (L0, L0+2)，即合并 (L0+L1) 和 (L2+L3)。
            # 结果存回 L0。
            # 此时数组的有效链表是 [ (L0+L1+L2+L3), ... ]
            # interval 变为 4。
            # 
            # 循环结束： interval (4) 不再小于 amount (4)。
            # ----------------------------------------------------
            
            # 扩大合并的步长，进入下一轮迭代（有效链表数量减半）
            interval *= 2
            
        # 最终合并的结果存储在 lists[0]
        return lists[0]

    def mergeTwoSortedListsIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        """标准函数：合并两个有序链表"""
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        # 连接剩余部分
        tail.next = l1 if l1 else l2
        
        return dummy.next
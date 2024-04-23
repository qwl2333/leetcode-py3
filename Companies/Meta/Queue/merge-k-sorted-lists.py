# lc 23
import heapq
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # merge k sorted lists using min heap
    # time O(nk*logk)   space O(k)   k: number of lists that need to be merged, n: average length of each list
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap, res = [], ListNode()
        for i, list in enumerate(lists):
            if list:
                heapq.heappush(heap, (list.val, i, list))

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
    
    # Merge sort
    # k : number of lists,  n: avg number of nodes in list  
    # time O(nk*logk) -  (height of stack)logk * nk (number of nodes we need to iterate)           
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
# lc 339
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
from collections import deque
class Solution:
    def __init__(self):
        self.count = 0

    # top down sol
    # Time O(n), space worst case O(n), [1,[2,[3,[4]]]]
    def depthSum(self, nestedList: list['NestedInteger']) -> int:
        for intg in nestedList:
            self.find_integers(intg, 1)
        return self.count
    
    def find_integers(self, nested_integer: 'NestedInteger', depth: int):
        if nested_integer.isInteger():
            self.count += nested_integer.getInteger() * depth
            return
        
        for intg in nested_integer.getList():
            self.find_integers(intg, depth + 1)

    # bottom up sol
    def depthSum2(self, nestedList: list['NestedInteger']) -> int:
        def depthSumHelper(nestedList: list['NestedInteger'], depth: int) -> int:
            sum = 0
            for itg in nestedList:
                if itg.isInteger():
                    sum += itg.getInteger() * depth
                else:
                    sum += depthSumHelper(itg.getList(), depth + 1)
            
            return sum
        
        return depthSumHelper(nestedList, 1)
    
    # BFS
    def depthSum3(self, nestedList: list['NestedInteger']) -> int:
        q = deque()
        res = 0
        q.append((nestedList, 1))
        
        while q:
            cur_list, cur_depth = q.popleft()
            for itg in cur_list:
                if itg.isInteger():
                    res += itg.getInteger() * cur_depth
                else:
                    q.append((itg.getList(), cur_depth + 1))
        
        return res
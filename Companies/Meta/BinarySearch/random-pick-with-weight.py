# lc 528
# https://www.youtube.com/watch?v=7x7Ydq2Wfvw&ab_channel=CrackingFAANG
import random
class Solution:
    # 假如w是[1，2，4]
    # 利用prefix sum得到[1，3，7]，那么[1,7]之间任意取一个数，比如是4，概率上属于在区间(3,7]之间即（4，5，6，7)，所以应该返回7的index也就是w里面4的index
    # s O(n), t O(n) n = len(w)
    def __init__(self, w: list[int]):
        self.prefix_sums = []
        total = 0
        for weight in w:
            total += weight
            self.prefix_sums.append(total)
        self.total = total

    # s O(1), t O(logn)
    def pickIndex(self) -> int:
        target = random.randint(1, self.total) # [1, self.total] 之间任意去一个数
        # 找第一个>= target的位置，也就是找可插入的lower bound
        # 还是[1,7]的例子，不管target是4 5 6 7最后要找的都是prefix_sum里面的7，但是
        # target是3, 找的就是prefix_sum里面的3，所以找的是在prefix_sum从左往右第一个>=target的
        l, r = 0, len(self.prefix_sums) - 1
        while l <= r:
            mid = (l + r) // 2
            if self.prefix_sums[mid] >= target:
                r = mid - 1
            else: # self.prefix_sums[mid] < target
                l = mid + 1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
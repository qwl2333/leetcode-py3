# lc 2817
import heapq
class Solution:
    """
    核心策略：数值排序 + 索引双堆
    1. 目标：找到 min|nums[i] - nums[j]| 且 |i - j| >= x
    2. 技巧：按数值从小到大遍历。这样对于当前值 val，所有在堆里的数都比它小。
    计算差值时就不需要 abs()，直接 val - historical_val 即可。
    3. 难点：如何快速找到满足索引距离 >= x 的历史数字？

    TC: O(N * logN)
    SC: O(N)
    """

    def minAbsoluteDifference(self, nums: list[int], x: int) -> int:
        # 1. 预处理：记录 (数值, 原始索引)，并按数值从小到大排序
        # 这样我们后续遍历时，当前 val 永远是最大的
        sorted_nums = sorted((val, i) for i, val in enumerate(nums))
        
        # heap_left: 最小堆，按索引排序，找出现在当前索引“左侧”且距离 >= x 的数 (j <= i - x)
        heap_left = [] 
        # heap_right: 最大堆，按索引排序，找出现在当前索引“右侧”且距离 >= x 的数 (j >= i + x)
        heap_right = []
        
        min_diff = float('inf')

        for val, index in sorted_nums:
            
            # 将当前处理过的数字放入两个堆中作为“历史记录”
            # 注意：此时堆里所有的数字 val_prev 都满足 val_prev <= val
            heapq.heappush(heap_left, (index, val)) 
            heapq.heappush(heap_right, (-index, val)) 

            # 逻辑 A：寻找左侧满足条件的数 (j + x <= index)
            # 如果堆顶索引 + x <= 当前索引，说明找到了一个合法的一对
            while heap_left and heap_left[0][0] + x <= index:
                # 贪心性质：因为 val 是递增的，当前 val 减去这个 heap_val 得到的是
                # 该 heap_val 能贡献的最小差值，后续的 val 只会更大，所以可以直接 pop
                prev_val = heapq.heappop(heap_left)[1]
                min_diff = min(min_diff, val - prev_val)
            
            # 逻辑 B：寻找右侧满足条件的数 (j - x >= index)
            # 转换公式：-j + x <= -index
            while heap_right and heap_right[0][0] + x <= -index:
                prev_val = heapq.heappop(heap_right)[1]
                min_diff = min(min_diff, val - prev_val)
            
            # 优化：如果已经找到差值为 0，直接收工
            if min_diff == 0:
                return 0
                
        return min_diff
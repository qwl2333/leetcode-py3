# lc 378 
# _count_le 计算矩阵中有多少个元素小于等于 target 和 lc 240 类似
import heapq
from typing import List

class Solution:
    # 辅助函数：计算矩阵中有多少个元素小于等于 target (O(2N) 时间复杂度)
    def _count_le(self, matrix: List[List[int]], target: int) -> int:
        N = len(matrix)
        count = 0
        
        # 从左下角开始 (r: row, c: col)
        r, c = N - 1, 0 
        
        # 沿着“阶梯”路径向上/右移动
        while r >= 0 and c < N:
            if matrix[r][c] <= target:
                # 1. 当前元素 <= target
                # 2. 由于列是有序的，matrix[r][c] 上方 r+1 个元素都 <= target
                count += r + 1 
                # 3. 移动到下一列 (向右)
                c += 1
            else:
                # 1. 当前元素 > target
                # 2. 由于行是有序的，当前行左侧的元素也 > target
                # 3. 移动到上一行 (向上)
                r -= 1
        
        return count

    '''
     TC: O(N * log(max - min))
     SC: O(1)
    '''
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        
        # 1. 确定搜索的值域 [low, high]
        low = matrix[0][0]
        high = matrix[N - 1][N - 1]
        
        # 最终答案将存储在 low 中
        while low <= high:
            mid = (high + low) // 2
            
            # 2. 计数：计算小于等于 mid 的元素个数
            count = self._count_le(matrix, mid)
            
            if count < k:
                # 小于等于 mid 的元素不足 k 个，说明 mid 太小了
                low = mid + 1
            else:
                # 小于等于 mid 的元素 >= k 个，说明 mid 可能是答案，或者答案在 [low, mid - 1] 范围内
                # 尝试向左收缩，寻找更小的潜在答案
                high = mid - 1
                
        return low
    
    '''
        假设矩阵维度为 N * N
        TC: O(K \ log N)
        总共k 次操作, 没吃操作包括从大小为N的堆中取出和放入元素
        堆操作的代价是O(logN)
        总时间复杂度为O(klogN)
        SC: O(N)
        用于存储最小堆, 最多只存储N个元素(每行一个)
    '''
    def kthSmallest_heap(self, matrix: List[List[int]], k: int) -> int:
        N = len(matrix)
        
        # 最小堆存储格式: (值, 行索引, 列索引)
        min_heap = []
        
        # 1. 初始化堆：将每一行的第一个元素放入堆中
        # 堆的大小最多为 N
        for r in range(N):
            # 将 (matrix[r][0], r, 0) 放入堆中
            # 只需处理第一列，因为每一行的最小值都在第一列
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
            
        # 2. 迭代 K-1 次，找到第 K 个最小元素
        kth_smallest = 0
        
        for _ in range(k):
            # 取出堆顶的最小元素及其坐标
            kth_smallest, r, c = heapq.heappop(min_heap)
            
            # 3. 检查当前行 r 是否还有下一个元素
            if c + 1 < N:
                # 如果有，将该行的下一个元素 (即右侧邻居) 放入堆中
                next_val = matrix[r][c + 1]
                heapq.heappush(min_heap, (next_val, r, c + 1))
                
        return kth_smallest
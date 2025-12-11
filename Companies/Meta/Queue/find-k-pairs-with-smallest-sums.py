# lc 373
import heapq
from typing import List

class Solution:
    '''
    tc: O(k * log(N1))
    sc: O(N1)
    '''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        N1 = len(nums1)
        N2 = len(nums2)
        
        # 结果数组
        result = []
        
        # 最小堆存储: (当前和, nums1索引 i, nums2索引 j)
        min_heap = []
        
        # 1. 初始化堆：将 nums1 中的每个元素与 nums2[0] 组成的数对放入堆中
        for i in range(N1): # 其实 range(min(N1, k)) 也行, 也很好理解 只需放入 min(N1, k) 个初始元素，因为更大的元素一开始肯定不会是最小的 k 个之一
            current_sum = nums1[i] + nums2[0]
            # 放入 (和, i, 0)
            heapq.heappush(min_heap, (current_sum, i, 0))
            
        # 2. 迭代 K 次，取出最小的数对, 其实这里不用判断min_heap是否为空, 以为k <= nums1.length * nums2.length
        # 如果k 可以无限大, 那这里就要注意判断min_heap是不是空了, 以为可能不够k次
        while k > 0 and min_heap:
            
            current_sum, i, j = heapq.heappop(min_heap)
            
            # 将数对加入结果
            result.append([nums1[i], nums2[j]])
            
            # 3. 探索下一个有潜力的数对
            # 下一个潜在的最小和数对是 (nums1[i], nums2[j+1])
            if j + 1 < N2:
                next_sum = nums1[i] + nums2[j + 1]
                # 放入 (下一个和, i, j+1)
                heapq.heappush(min_heap, (next_sum, i, j + 1))
            k -= 1
                
        return result
# lc 480 此题和295很类似, 都是利用一个最大堆存小的一半, 用最小堆存大的一半, 这样可以轻易从 -small[0], large[0] 中得到 median值
import heapq
from collections import defaultdict

class Solution:
    '''
    N 是 nums的长度
    为什么时间复杂度是 O(N log N)
    我们要对整个数组进行滑动，窗口从左移到右：总步数：窗口一共移动了约 N 次。
    每一步的操作: 进堆(heappush): log(堆的大小)
                出堆(heappop):  log({堆的大小})
                堆的大小: 虽然窗口只有 K 那么大，但因为我们使用了延迟删除，那些本该被删掉的数可能还堆在里面。在最坏情况下，堆的大小会接近 N。
    结论:  N 次操作 * log N 的堆操作 = O(N log N)。

    为什么空间复杂度是O(N)
    延迟删除带来的代价
        理想情况: 如果能立刻删除掉多余的数 空间应该是O(K) 因为只存窗口的数
    延迟删除的情况:
        堆 small, large: 由于过期的数没到堆顶不会被弹出 堆的体积会不断膨胀 最坏情况下 堆里塞满了几乎整个数组
        哈希表 delayed: 为了记录那些数据要删除, 字典里最多可能存下所有滑出窗口的数, 规模也是O(N)
    '''
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        # small 是大顶堆（存负数），large 是小顶堆
        small, large = [], []
        # 用 defaultdict(int) 记录那些滑出窗口、待从堆中删除的数字及其次数
        delayed = defaultdict(int)
        
        # 记录堆中“有效元素”的数量，因为堆里会有还没来得及删除的“脏数据”
        small_size, large_size = 0, 0

        # 辅助函数：弹出堆顶所有“待删除”的元素
        def prune(heap, is_small):
            while heap:
                num = -heap[0] if is_small else heap[0]
                if delayed[num] > 0:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        # 保持两个堆的平衡：small_size == large_size 或 small_size == large_size + 1
        def rebalance():
            nonlocal small_size, large_size
            if small_size > large_size + 1:
                val = -heapq.heappop(small)
                heapq.heappush(large, val)
                small_size -= 1
                large_size += 1
                prune(small, True)
            elif small_size < large_size:
                val = heapq.heappop(large)
                heapq.heappush(small, -val)
                small_size += 1
                large_size -= 1
                prune(large, False)

        def add_num(num):
            nonlocal small_size, large_size
            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1
            rebalance()

        def remove_num(num):
            nonlocal small_size, large_size
            delayed[num] += 1
            if num <= -small[0]:
                small_size -= 1
                if num == -small[0]:
                    prune(small, True)
            else:
                large_size -= 1
                if num == large[0]:
                    prune(large, False)
            rebalance()

        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2.0

        # 1. 初始化第一个窗口
        for i in range(k):
            add_num(nums[i])
        
        res = [get_median()]

        # 2. 开始滑动窗口
        for i in range(k, len(nums)):
            add_num(nums[i])          # 进一个新数
            remove_num(nums[i - k])   # 标记删掉滑出窗口的数
            res.append(get_median())
            
        return res
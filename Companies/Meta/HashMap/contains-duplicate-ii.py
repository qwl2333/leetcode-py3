# lc 219
class Solution:
    '''
    用一个 dict：last_index[val] = 最近一次看到 val 的下标

    遍历 nums：

        如果 val 之前见过，并且 i - last_index[val] <= k → 直接返回 True

        不然就更新：last_index[val] = i

    遍历完还没返回，就 False
    T O(N)
    S O(N)
    '''
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_index = {}

        for i, val in enumerate(nums):
            if val in last_index and i - last_index[val] <= k:
                return True
            last_index[val] = i

        return False
    
    '''
    保持一个大小最多为 k 的窗口，里面是“最近 k 个元素”的集合：

    遍历 nums：

        如果 nums[i] 已经在 window 里 → 说明之前的某个相同元素到现在距离 ≤ k → 返回 True

        否则：把 nums[i] 加入 window

        如果 window 的大小 > k：把最左边那个元素（nums[i-k]）从 window 删除
    
    T O(N)
    S O(K) window 最多k+1个元素
    '''
    def containsNearbyDuplicate_sliding_window(self, nums: list[int], k: int) -> bool:
        window = set()

        for i, val in enumerate(nums):
            if val in window:
                return True
            
            window.add(val)

            if len(window) > k:
                window.remove(nums[i - k])

        return False


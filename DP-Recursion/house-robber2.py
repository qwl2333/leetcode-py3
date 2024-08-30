class Solution:
    '''
    就是 house robber1 跑两次 一次是nums[1:]，去掉第一个元素，一次是nums[:-1]，去掉最后一个元素
    为什么跑两次，因为环的存在，抢劫的结果不可能同时抢第一个和最后一个，只能选一个，要么nums[1:]，要么nums[:-1]
    '''

    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1: # 单独判读只有一个元素，因为nums[1:] nums[:-1]为空array如果只有一个元素
            return nums[0]
    
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        pre_rob2, pre_rob1 = 0, 0 # pre_rob1是往前倒一次，pre_rob2是往前倒2次

        for n in nums:
            cur_rob = max(pre_rob2 + n, pre_rob1)
            pre_rob2 = pre_rob1
            pre_rob1 = cur_rob
        
        return pre_rob1


 

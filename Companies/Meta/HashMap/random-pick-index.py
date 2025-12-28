# lc 398
# https://www.youtube.com/watch?v=HXRN8ZfAQOI&ab_channel=CrackingFAANG
import random
from collections import defaultdict
class Solution:
    # 肯定是这个好，第二个Reservoir Sampling 适用于 nums 太大了 以至于内存存不下 indices 这样的dict, 或者 数组是一个stream
    # t O(n), s O(n)
    def __init__(self, nums: list[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    # t O(1)
    def pick(self, target: int) -> int:
        indices_for_target = self.indices[target]
        random_pick = random.randint(0, len(indices_for_target) - 1)
        return indices_for_target[random_pick]

'''
如果数组非常大（大到内存装不下索引字典），或者数组是一个流（Stream）（一直在增加，无法预处理），那么只有水塘抽样能解决问题，因为它不需要额外的内存来存储位置信息
'''
class SolutionReservoirSampling:
    # t O(1) s O(n)
    def __init__(self, nums: list[int]):
        self.nums = nums

    # t O(n)
    def pick(self, target: int) -> int:
        count = 0
        index = -1
        for i, num in enumerate(self.nums):
            if num != target:
                continue
            count += 1
            random_count = random.randint(1, count)
            if random_count == count:
                index = i
        return index
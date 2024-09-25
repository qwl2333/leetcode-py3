# lc 398
# https://www.youtube.com/watch?v=HXRN8ZfAQOI&ab_channel=CrackingFAANG
import random
from collections import defaultdict
class Solution:
    # 肯定是这个好，第二个Reservoir Sampling纯纯炫技
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
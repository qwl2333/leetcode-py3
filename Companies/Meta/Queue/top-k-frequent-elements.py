# lc 347
from heapq import heappush, heappop
class Solution:
    # time O(logk*n), space O(n)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        min_heap = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, freq in freq.items():
            heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heappop(min_heap)

        res = []
        while min_heap:
            res.append(heappop(min_heap)[1])
        
        return res

    # Time O(n)  Space O(n)  n = len(nums)
    def topKFrequentBucketSort(self, nums: list[int], k: int) -> list[int]:
        bucket = [[] for _ in range(len(nums) + 1)]

        freq_map = {}
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for num, freq in freq_map.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(nums), -1, -1):
            if not bucket[i]:
                continue
            res.extend(bucket[i])
            if len(res) == k:
                break

        return res

s = Solution()
print(s.topKFrequentBucketSort([1,1,1,2,2,3], 2))
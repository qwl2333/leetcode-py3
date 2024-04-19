# lc 1570
class SparseVector:
    # We could use hashmap, but if nums is dense map could be super large
    # Time O(n), space O(l) n: number of elements in nums, l, number of non-zero elements in nums
    def __init__(self, nums: list[int]):
        self.idx_val = []
        for idx, num in enumerate(nums):
            if num == 0:
                continue
            self.idx_val.append((idx, num))

    # Return the dotProduct of two sparse vectors
    # Time O(l1 * log(l2)) l1, l2 are the number of non-zero elements in two nums
    def dotProduct(self, vec: 'SparseVector') -> int:
        cur_vec = self.idx_val
        tgt_vec = vec.idx_val # assume tgt_vec is dense
        res = 0
        for cur_idx, cur_v in cur_vec:
            target_val = self.binary_search(cur_idx, tgt_vec)
            if target_val != -1:
                res += cur_v * target_val
        return res
    
    def binary_search(self, cur_idx: int, target_idx_val: list):
        l, r = 0, len(target_idx_val) - 1
        while l <= r:
            mid = (l + r) // 2
            if cur_idx == target_idx_val[mid][0]:
                return target_idx_val[mid][1]
            elif cur_idx < target_idx_val[mid][0]:
                r = mid - 1
            else:
                l = mid + 1
            
        return -1 # nums[i] from [0, 100]


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
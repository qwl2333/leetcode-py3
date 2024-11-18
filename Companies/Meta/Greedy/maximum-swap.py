# lc 670
class Solution:
    # 和31 next permutation做区分, 31是找下一个排列刚好大于num，所以是尽可能小
    # 670是一次swap,尽可能的大
    # 最优解 one pass
    # T O(n) S O(n)
    def maximumSwap2(self, num):
        num_str = list(str(num))
        n = len(num_str)
        max_i, max_n = n - 1, num_str[n - 1]
        left, right = -1, -1
        for i in range(len(num_str)-2, -1, -1):
            if num_str[i] == max_n:
                continue

            if num_str[i] > max_n:
                max_n = num_str[i]
                max_i = i
            else: # num_str[i] < max_n
                left = i
                right = max_i

        if left == -1:
            return num
        else:
            num_str[left], num_str[right] = num_str[right], num_str[left]
            return int("".join(num_str))

    # T: O(n), S: O(n)
    def maximumSwap(self, num: int) -> int:
        num_str = list(str(num)) # ['2','1','3','2']
        bucket = [-1 for i in range(10)] # bucket是mapping from value to idx，这个idx会被更右的idx覆盖掉，比如两个‘2’
                                         # 因为相同的值，肯定是用更右边的拿来swap，（greedy）
                                         # bucket作用是找一个idx来swap
        for idx, d_str in enumerate(num_str):
            digit = int(d_str)
            bucket[digit] = idx
        # bucket: [-1, 1, 3, 2, -1, -1, -1, -1, -1, -1]
        #           0  1  2  3   4   5   6   7   8   9

        for idx, d_str in enumerate(num_str):
            digit = int(d_str)
            for i in range(9, digit, -1):
                idx_to_swap = bucket[i]
                if idx_to_swap > idx:
                    num_str[idx_to_swap], num_str[idx] = num_str[idx], num_str[idx_to_swap]
                    return int(''.join(num_str))

        return num

s = Solution()
print(s.maximumSwap2(12))
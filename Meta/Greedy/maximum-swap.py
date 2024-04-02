# lc 670
class Solution:
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
    
    # 找第一个严格递增的点，为什么呢，因为递减或者相等的情况下不需要swap
    # 第一个严格递增点右边找最大值max_val，如有多个max_val, 找最右那个(greedy)
    # 第一个严格递增点最左边小于max_val, 和max_val的idx去swap
    # 为什么是第一个严格递增点，greedy思想235689，肯定是2用来swap
    def maximumSwapGreedy(self, num: int) -> int:
        numList = list(str(num))

        # Find index where numList[i] < numList[i+1], meaning a chance to flip
        for i in range(len(numList)-1):
            if numList[i] < numList[i+1]:
                break
        # If nothing found, return num
        else: # for else语句，else语句会在for loop结束后执行，但是如果for loop break了，else语句不会执行
            # 如果所有element numList[i] >= numList[i+1] 说明是递减的数，9998765555，不需要swap
            return num
        
        # Keep going right to find the maximum value index
        maxIdx, maxVal = i+1, numList[i+1]
        for j in range(i+1, len(numList)):
            if maxVal <= numList[j]: # 注意这里的等号，要找最右的最大值 2999，肯定是找最右的那个9
                maxIdx, maxVal = j, numList[j]

        # Going right from i, find left-most value that is less than maxVal
        leftIdx = i
        for j in range(i, -1, -1):    
            if numList[j] < maxVal: # 肯定要严格小于maxVal,相等没有swap的意义
                leftIdx = j

        # Swap maximum after i and left-most less than max
        numList[maxIdx], numList[leftIdx] = numList[leftIdx], numList[maxIdx]

        # Re-create the integer
        return int(''.join(numList))  

s = Solution()
print(s.maximumSwapGreedy(2132))
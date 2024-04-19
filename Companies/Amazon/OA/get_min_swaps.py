class Solution:
# https://leetcode.com/discuss/interview-question/2561958/Amazon-AWS-or-Vancouver-Canada-or-OA
# 题目意思是给一个array，问最小swap多少次可以保证,swap只能相邻的元素swap
# plates[1] < plates[i] for all (2 <= i <= n)
# plates[i] < plates[n] for all (1 <= i <= n-1) 
# 所有元素都不相同
    def get_min_swaps(self, arr: list[int]) -> int:
        n = len(arr)
        min_value = arr[0]
        min_idx = 0
        max_value = arr[n - 1]
        max_idx = n - 1
        for i in range(n):
            if arr[i] < min_value:
                min_value = arr[i]
                min_idx = i
            
            if arr[i] > max_value:
                max_value = arr[i]
                max_idx = i
        if max_idx > min_idx:
            return min_idx + (n - 1) - max_idx
        else:
            return min_idx + (n - 1) - max_idx - 1
    
s = Solution()
print(s.get_min_swaps([4,5,3,2,1,8,7,6]))

class Solution:
# https://leetcode.com/discuss/interview-question/2561958/Amazon-AWS-or-Vancouver-Canada-or-OA
# 题目意思是给一个array，问最小swap多少次可以保证所有元素递增
# 所有元素都不相同
# https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/
# 答案就是找环，swap的次数等于环里面node的个数-1
    def get_min_swaps(self, arr: list[int]) -> int:
        n = len(arr)
        original_pos_to_value = {} # original arr, pos to value
        sorted_value_to_pos = {} # sorted arr, value to pos

        for idx, v in enumerate(arr):
            original_pos_to_value[idx] = v
        print(original_pos_to_value)

        sorted_arr = sorted(arr)
        for idx, v in enumerate(sorted_arr):
            sorted_value_to_pos[v] = idx
        
        print(sorted_value_to_pos)

        count = 0
        visited = [False for i in range(n)]
        for idx in range(n):
            occupied_idx = idx
            cycle_size = 0
            while not visited[occupied_idx]:
                visited[occupied_idx] = True
                cycle_size += 1
                original_value = original_pos_to_value[occupied_idx]
                occupied_idx = sorted_value_to_pos[original_value]
            print(f'cycle size {cycle_size}')
            if cycle_size > 0:
                count += cycle_size - 1
        
        return count

    
s = Solution()
print(s.get_min_swaps([4,5,1,2,3]))

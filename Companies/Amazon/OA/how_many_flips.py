class Solution:
    # 题目是给一串0000..0，flip到target要的最小步数
    # 第一反应是bfs 层级遍历求层数
    # 但是可以o(n)，只需要遍历一遍就行 
    def min_number_of_flips(self, target: str) -> int:
        cur = 0
        steps = 0
        for t in target:
            t_num = int(t)
            if t_num == cur:
                continue
            cur = cur ^ 1
            steps += 1
        
        return steps

s = Solution()
print(s.min_number_of_flips('01011'))

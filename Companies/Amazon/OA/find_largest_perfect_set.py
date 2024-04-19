from collections import deque
class Solution:
    # 题目是给你一个数字array, 所有数字都是unique，找到里面最大的连续的 a, a^2, (a^2)^2...，比如2，4，16
    # 解法是bfs找 >=2 的最长距离
    # 要注意包含1的情况，1其实不能算，因为1只有1的最长距离
    def find_largest_perfect_set(self, onion_bags: list[int]) -> int:
        arr_set = set(onion_bags)
        if 1 in arr_set:
            arr_set.remove(1)
        
        queue = deque(onion_bags)
        level = 0
        while queue:
            size = len(queue)
            for _i in range(size):
                cur = queue.popleft()
                if cur ** 2 in arr_set:
                    queue.append(cur ** 2)
            level += 1
            
        return level if level >= 2 else -1

s = Solution()
print(s.find_largest_perfect_set([2,3,4,9,16]))

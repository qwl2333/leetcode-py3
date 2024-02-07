# lc 542
from typing import List
from collections import deque
class Solution:
    # multi-source BFS timne O(m * n) space O(m * n) worst case all cells added to the queue
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        num_of_r = len(mat)
        num_of_c = len(mat[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        res = [[float('inf') for _ in range(num_of_c)] for _ in range(num_of_r)]
        queue = deque()

        for i in range(num_of_r):
            for j in range(num_of_c):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    queue.append((i, j))
    
        while queue:
            cur_r, cur_c = queue.popleft()
            for dx, dy in directions:
                new_r = cur_r + dx
                new_c = cur_c + dy
                if 0 <= new_r < num_of_r and 0 <= new_c < num_of_c:
                    if res[cur_r][cur_c] + 1 < res[new_r][new_c]:
                        res[new_r][new_c] = res[cur_r][cur_c] + 1
                        queue.append((new_r, new_c))
        
        return res

s = Solution()
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))

# lc 200
from typing import List
from collections import deque
class Solution:
    # BFS grid has n*m 节点，大约 2*n*m 条edges， 所以 time O(n*m) ， space O(n*m)
    def numIslandsBFS(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        count = 0
        def bfs(grid: List[List[str]], col: int, row: int):
            queue = deque([(col, row)])
            grid[col][row] = '0'
            while queue:
                x, y = queue.popleft() # 如果改成queue.pop(), 就是iterative的dfs
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == '1':
                        grid[new_x][new_y] = '0'
                        queue.append((new_x, new_y))

        # dfs 方法 和 bfs差不多意思
        def dfs(grid: List[List[str]], x: int, y: int):
            grid[x][y] = '0'

            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < n and 0 <= new_y < m and grid[new_x][new_y] == '1':
                    dfs(grid, new_x, new_y)
                
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1': # 这里就包含了只会visit还没有visit过的1，visited 1都变成了0，如果用visited = set，这里要记得check if visited
                    bfs(grid, i, j)
                    count += 1

        return count
        
s = Solution()
print(s.numIslandsBFS([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))

# lc 994
from collections import deque
class Solution:
    # Time O(n * m) each cell visited once,  Space O(n * m) worst case all oranges are rotten, all of them need to added to queue
    def orangesRotting(self, grid: list[list[int]]) -> int:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        # visited = [[0 for _ in range(m)] for _ in range(n)]
        mins = -1
        queue = deque()
        num_of_good_oranges = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    num_of_good_oranges += 1

        if num_of_good_oranges == 0:
            return 0

        while queue:
            size = len(queue)
            for i in range(size):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c))
            mins += 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        
        return mins

s = Solution()

print(s.orangesRotting([[2,1,1]]))

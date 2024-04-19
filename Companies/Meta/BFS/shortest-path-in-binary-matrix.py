from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 0 and n == 1:
            return 1
    
        directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        queue = deque()
        visited = set()
        if grid[0][0] == 0:
            queue.append((0, 0))
            visited.add((0, 0))

        steps = 0
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    new_x = x + dx
                    new_y = y + dy
                    if 0 <= new_x < n and 0 <= new_y < n and (new_x, new_y) not in visited and grid[new_x][new_y] == 0:
                        if new_x == n - 1 and new_y == n - 1:
                            return steps + 2
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))
            steps += 1
        return -1

s = Solution()
print(s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))
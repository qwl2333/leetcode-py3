# lc 63
class Solution:
    # 我自己想的解法，brute force的解法， top down 的dfs
    # t O(n*m) 看起来指数，每次两个选择向右或者向下，实际上理想情况下没有任何障碍，所有可能性加起来n*m
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        dirs = [[0, 1], [1, 0]]
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        self.count = 0

        def find_star(x: int, y: int):
            if x == n - 1 and y == m - 1 and obstacleGrid[x][y] == 1:
                self.count += 1
                return
            
            for dx, dy in dirs:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < n and 0 <= new_y < m and obstacleGrid[new_x][new_y] == 0:
                    obstacleGrid[new_x][new_y] = 1
                    find_star(new_x, new_y)
                    obstacleGrid[new_x][new_y] = 0
        if obstacleGrid[0][0] == 0:
            obstacleGrid[0][0] = 1
            find_star(0, 0)
        return self.count
    
    # T: O(n * m), space O(n * m)
    # neetcode 解法，bottom up的dfs + dp
    def uniquePathsWithObstaclesDP(self, obstacleGrid: list[list[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = {}

        def get_number_of_unique_paths(x: int, y: int) -> int:
            if x == n or y == m or obstacleGrid[x][y] == 1:
                return 0
            if x == n - 1 and y == m - 1:
                return 1
            if (x, y) in dp:
                return dp[(x, y)]
            
            left = get_number_of_unique_paths(x, y + 1)
            down = get_number_of_unique_paths(x + 1, y)
            dp[(x, y)] = left + down
            return dp[(x, y)]
        
        return get_number_of_unique_paths(0, 0)

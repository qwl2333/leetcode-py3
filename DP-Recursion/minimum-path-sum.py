# lc 64
class Solution:
    # Time O(n * m), Space O(n * m)
    def minPathSum(self, grid: list[list[int]]) -> int:
        '''
        grid:
        [
            [1,3,1],
            [1,5,1],
            [4,2,1]
        ]

        dp[i][j] - path from 0,0 -> i,j with min path sum
        [
            [1,4,5],
            [2,7,6],
            [6,8,7]
        ]

        '''

        n = len(grid)
        m = len(grid[0])
        dp = [[0 for _ in range(m)] for _ in range(n)] # 

        for i in range(0, n):
            for j in range(0, m):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] + grid[i][j]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        
        return dp[n - 1][m - 1]

s = Solution()
print(s.minPathSum([
            [1,3,1],
            [1,5,1],
            [4,2,1]
        ]))
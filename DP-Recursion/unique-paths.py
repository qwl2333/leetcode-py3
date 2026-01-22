# lc 62
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. 初始化 dp 数组，初始值设为 1
        # 因为到达第一行和第一列的任何位置都只有 1 条路径（一直往右或一直往下）
        dp = [[1] * n for _ in range(m)]
        
        # 2. 从 (1, 1) 开始填表
        for r in range(1, m):
            for c in range(1, n):
                # 当前格子的路径数 = 左边格子 + 上边格子
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        # 3. 返回右下角的值
        return dp[m-1][n-1]
    
    # 简化到只需要一行的额外空间
    def uniquePathsOptimized(self, m: int, n: int) -> int:
        # 只维护一行的数据
        row = [1] * n
        
        for r in range(1, m):
            for c in range(1, n):
                # row[c] 代表当前位置“上方”的值
                # row[c-1] 代表当前位置“左边”的值
                row[c] = row[c] + row[c-1]
                
        return row[n-1]
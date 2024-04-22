# Given two 1*m arrays A and B to form a 2*m grid, move only right and down from (0,0) → (1, m - 1) to get a path.

# The optimal path is path with minimum sum of path values. Get max value over the optimal path

# Example:

# [

# [-5, -1, -3],

# [-5, 5, -2]

# ]

# path -5, -1, -3, -2 is optimal because it has minimum sum -11, the maximum value of this path is -1, so the result is -1

# 此题是1102. Path With Maximum Minimum Value 和 64. Minimum Path Sum的结合

class Solution:
    # Time O(2 * m), space O(2 * m) m - number of columns in Array A and B
    def get_max_value_over_a_optimal_path(self, A: list[int], B: list[int]) -> int:
        m = len(A)
        dp = [[(0, 0) for _ in range(m)] for _ in range(2)] # dp[i][j]: (min_sum, max_valuie), 
                                                            # min_sum is min sum from (0,0) -> (i, j), 
                                                            # max_value is max value in the path
        
        '''
        grid combined by A and B:
            [
                [-5, -1, -3],
                [-5, 5, -2]
            ]
    
        dp
            [
                [(-5, -5), (-6, -1), (-9, -1)],
                [(-10, -5), (-5, 5), (-11, -1)]
            ]
        
        -11 is min sum of the path, -1 is the max value of this path
        '''

        for i in range(2):
            for j in range(m):
                if i == 0 and j == 0:
                    dp[0][0] = (A[0], A[0])
                elif i == 0:
                    dp[i][j] = (dp[i][j - 1][0] + A[j], max(dp[i][j - 1][1], A[j]))
                elif j == 0:
                    dp[i][j] = (dp[i - 1][j][0] + B[j], max(dp[i - 1][j][1], B[j]))
                else:
                    if dp[i - 1][j][0] < dp[i][j - 1][0]:
                        dp[i][j] = (dp[i - 1][j][0] + B[j], max(dp[i - 1][j][1], B[j]))
                    elif dp[i - 1][j][0] > dp[i][j - 1][0]:
                        dp[i][j] = ((dp[i][j - 1][0] + B[j], max(dp[i][j - 1][1], B[j])))
                    else: # dp[i - 1][j][0] == dp[i][j - 1][0]
                        dp[i][j] = ((dp[i][j - 1][0] + B[j], max(dp[i][j - 1][1], dp[i - 1][j][1], B[j])))

        return dp[1][m - 1][1]

s = Solution()
print(s.get_max_value_over_a_optimal_path(
                [2],
                [1]
            ))
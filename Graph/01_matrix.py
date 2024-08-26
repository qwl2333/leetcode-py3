# lc 542
from typing import List
from collections import deque
class Solution:
    # 烂橘子法
    # 此题可以看成从0开始向周围感染，第一天感染的就是距离为1的，第二天感染就是距离为2
    # BFS timne O(m * n) space O(1)
    def updateMatrixBestSol(self, mat: list[list[int]]) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]] # d, r, u, l
        q = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] != 0:
                    mat[i][j] = -1 # 标记mat里面1为-1就是表示没有visited过，省掉了visited set，也可以和最后距离为1的区别开
                else:
                    q.append((i, j))

        steps = 1
        while q:
            size = len(q)
            for _ in range(size):
                x, y = q.popleft()
                for dx, dy in directions:
                    newx = x + dx
                    newy = y + dy
                    if 0 <= newx < n and 0 <= newy < m and mat[newx][newy] == -1:
                        mat[newx][newy] = steps
                        q.append((newx, newy))
            steps += 1
        
        return mat

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


    # dfs + memo backtracking
    def updateMatrix2(self, mat: list[list[int]]) -> list[list[int]]:
        n = len(mat)
        m = len(mat[0])
        directions = [[0, -1], [1, 0], [0, 1], [-1, 0]] # l d r u
        res = [[0 for i in range(m)] for j in range(n)]
        memo = {}

        def find_closest_zero(x: int, y: int, path: set):
            if mat[x][y] == 0:
                return 0
            if (x, y) in memo:
                return memo[(x, y)]

            initial_dis = 2 * (10 ** 4)
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                if n > new_x >= 0 and m > new_y >= 0 and (new_x, new_y) not in path:
                    path.add((new_x, new_y))
                    initial_dis = min(initial_dis, 1 + find_closest_zero(new_x, new_y, path))
                    path.remove((new_x, new_y))
            
            return initial_dis

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    continue
                path = set()
                path.add((i, j))
                clset = find_closest_zero(i, j, path)
                memo[(i, j)] = clset
                res[i][j] = clset
        
        return res

s = Solution()

mat =[[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]

print(s.updateMatrix2(mat))

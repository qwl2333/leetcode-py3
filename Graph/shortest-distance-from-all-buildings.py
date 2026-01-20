# lc 317 题目意思就是 找一个空地建房子，使得房子到所有building的距离和最小
from collections import deque

class Solution:
    # 假设M为行数，N为列数，K 为建筑数量。
    # 时间复杂度 (TC)：O(K * M * N)
    #   你需要为每一个建筑（最多 M * N 个）跑一次全图 BFS
    #   在最坏情况下，这会达到 O(M^2 * N^2)
    # 空间复杂度 (SC)：O(M * N)

    # 对每个建筑跑一次 BFS
    # 每一轮 BFS 只访问上一轮 BFS 能够到达的空地。这样可以自动过滤掉那些无法到达所有建筑的死角。
    def shortestDistance(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        total_dist = [[0 for _ in range(cols)] for _ in range(rows)]

        walkable_val = 0
        min_res = float('inf')

        def bfs(start_r: int, start_c: int) -> int:
            queue = deque()
            queue.append((start_r, start_c, 0))
            current_step_min = float('inf')

            while queue:
                r, c, dist = queue.popleft()

                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc

                    # pruning：只走向上一轮建筑也能到达的空地 (即 grid[nr][nc] == walkable_val)
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == walkable_val:
                        # 原地标记：表示这个空地已经被当前建筑“盖章”了,比如第一次0 -> -1， 下一次 -1 -> -2，这个值和下一次bfs的walkable_val是相同的
                        grid[nr][nc] -= 1
                        new_dist = dist + 1
                        queue.append((nr, nc, new_dist))

                        total_dist[nr][nc] += new_dist
                        # 更新当前这轮 BFS 结束后的全局最小距离候选值
                        current_step_min = min(current_step_min, total_dist[nr][nc])
            
            return current_step_min

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # 每遇到一个building，跑一次 BFS
                    min_res = bfs(r, c)
                    # 如果某次 BFS 后 min_res 还是 inf，说明有空地无法到达这个建筑, 或者根本没有空地
                    if min_res == float('inf'):
                        return -1
                    walkable_val -= 1
        
        return min_res if min_res != float('inf') else -1
    
    # tc rc 不变
    # 比较直观的没有pruning的解法，没有利用walkable_val来记录之前bfs走过的点
    # 我觉得这个更好
    def shortestDistanceNoPruning(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        # total_dist[r][c] 存储空地 (r, c) 到所有能到达它的建筑的距离总和
        total_dist = [[0] * cols for _ in range(rows)]
        # reach_count[r][c] 存储有多少个建筑可以到达空地 (r, c)
        reach_count = [[0] * cols for _ in range(rows)]
        total_buildings = 0
        
        def bfs(start_r, start_c):
            rows, cols = len(grid), len(grid[0])
            queue = deque([(start_r, start_c, 0)])
            visited = {(start_r, start_c)} # 每一轮 BFS 使用独立的 visited 集合
            
            while queue:
                r, c, d = queue.popleft()
                
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    
                    # 越界检查 + 未访问检查
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        
                        # 只有空地是可以穿过并计入距离的
                        if grid[nr][nc] == 0:
                            reach_count[nr][nc] += 1
                            total_dist[nr][nc] += d + 1
                            queue.append((nr, nc, d + 1))
                        # 注意：如果是 1（建筑）或 2（障碍物），BFS 不能穿过它们

        # 1. 对每个建筑分别进行 BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total_buildings += 1
                    bfs(r, c) # 发现建筑，立即开启该源点的 BFS

        # 2. 遍历所有格子，找到满足条件的最小距离
        min_dist = float('inf')
        for r in range(rows):
            for c in range(cols):
                # 条件：必须是空地，且必须能被所有建筑到达
                if grid[r][c] == 0 and reach_count[r][c] == total_buildings:
                    min_dist = min(min_dist, total_dist[r][c])
        
        return min_dist if min_dist != float('inf') else -1
# lc 778 题目意思是随着时间流逝，水会上涨，比如上涨到t，那所有高低小于等于t的都可以游过去，游泳的时间不用考虑， 求最小的可以游过去的时间
# 实际上要求找到从左上角到右下角的路径，使得路径上经过的所有格子中，海拔最高的那一个值尽可能小。
from heapq import heappop, heappush 

class Solution:
    # 复杂度分析:
    #    - 时间复杂度 (TC): O(N^2 log N)
    #      网格共有 N^2 个点，每个点入队出队一次，优先队列操作为 log(N^2) 即 2logN。
    #    - 空间复杂度 (SC): O(N^2)
    #      用于存储 visited 集合和优先队列。
    #  Dijkstra 改良版本
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # pq存的是: (从起点到当前路径的最大高度)
        pq = []
        heappush(pq, (grid[0][0], 0, 0))
        visited = {(0, 0)}

        # 如果需要记录路径, 那还需记录前驱节点: key 是 (nr, nc), value 是 (r, c)
        predecessors = {(0, 0): None}

        while pq:
            # 每次取出当前代价最小的点
            max_h, r, c = heappop(pq)

            # 只要到达终点，当前的 max_h 就是答案
            if r == n - 1 and c == n - 1:
                # 如果需要记录路径, 还原并打印路径
                path = self._reconstruct_path(predecessors, (n - 1, n - 1))
                print(f"找到的最优路径为: {' -> '.join([f'({pr},{pc})[H:{grid[pr][pc]}]' for pr, pc in path])}")
                return max_h
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))

                    # 如果需要记录路径, 记录这个邻居是从 (r, c) 走过去的
                    predecessors[(nr, nc)] = (r, c)

                    # 关键逻辑：新坐标到起点的最大高度是 (旧坐标最大高度) 和 (新格子高度) 的较大者
                    new_max = max(max_h, grid[nr][nc])
                    heappush(pq, (new_max, nr, nc))
        
        return -1

    def _reconstruct_path(self, predecessors: dict, end: tuple) -> list[tuple]:
            """
            从终点逆向回溯到起点
            """
            path = []
            curr = end
            while curr is not None:
                path.append(curr)
                curr = predecessors[curr]
            return path[::-1] # 翻转得到从起点到终点的顺序

# import heapq

# class Solution:
    # 这是bfs扩散找一个点(n-1, n-1), 到这个点时， 一定路径上的经过所有点的最大的值一定是最小的 相比其他路径
    def swimInWater_BFS(self, grid: list[list[int]]) -> int:
        n = len(grid)
        # pq 存储: (从起点到当前路径上的最大高度, r, c)
        pq = [(grid[0][0], 0, 0)]
        visited = set([(0, 0)])
        
        # 结果记录
        res = 0
        
        while pq:
            h, r, c = heappop(pq)
            
            # 更新全局经历过的最大高度
            res = max(res, h)
            
            # 到达终点，提前退出
            if r == n - 1 and c == n - 1:
                return res
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    # 将邻居的高度放入堆中，堆会自动帮我们选出接下来海拔最低的路
                    heappush(pq, (grid[nr][nc], nr, nc))
        return res
#
# TC: O(n^2 * logn)。总共有 n^2 个格子，每个格子进出堆一次。SC: O(n^2)。存储 visited 集合和堆。




#  Dijkstra 未改良版本, 事实上不需要记录min_max_height = [[float('inf')] * n for _ in range(n)], 因为按顺序出来的点的最小路径最大值分别是1,3, 
#  假如他们分别可以到达最小路径最大值为2的点，那一定是先出来的1->2是更短的路径相对3->2, 因为对于2来说 1->2 那最小路径最大是2，3->2则是3
#  所以改良版去掉了这个而是用visited
# import heapq

# class Solution:
#     def swimInWater(self, grid: list[list[int]]) -> int:
#         n = len(grid)
#         # pq 存储: (从起点到当前路径上的最大高度, r, c)
#         pq = [(grid[0][0], 0, 0)]
        
#         # 记录到达每个位置所需的“最小最大高度”
#         # 相当于 Dijkstra 里的 min_dist
#         min_max_height = [[float('inf')] * n for _ in range(n)]
#         min_max_height[0][0] = grid[0][0]
        
#         while pq:
#             path_max, r, c = heapq.heappop(pq)
            
#             if r == n - 1 and c == n - 1:
#                 return path_max # 这里的 path_max 就是答案
            
#             if path_max > min_max_height[r][c]:
#                 continue
                
#             for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#                 nr, nc = r + dr, c + dc
#                 if 0 <= nr < n and 0 <= nc < n:
#                     # 【关键点】：到达邻居的代价，是当前路径最大值和邻居海拔的较大者
#                     new_path_max = max(path_max, grid[nr][nc])
                    
#                     if new_path_max < min_max_height[nr][nc]:
#                         min_max_height[nr][nc] = new_path_max
#                         heapq.heappush(pq, (new_path_max, nr, nc))
#         return -1
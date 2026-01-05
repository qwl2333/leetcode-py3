# BFS	            无权图最短路	   边权全部相等时最快。
# Dijkstra	        单源所有点最短路	边权非负，算出起点到所有点的最短路径。 算法解释 python实现 https://www.youtube.com/watch?v=8POyTJu-XHw
# Bellman-Ford	    单源所有点最短路	可以处理负权边。                   算法解释 python 实现 https://www.youtube.com/watch?v=YklWOOAR6rs&list=PLqZkRM3t-8wZ3QBcq-xRDjhOzhdM7hW5w&index=16
# Floyd-Warshall	多源所有点最短路	算出图中任意两点之间的最短路径。      算法解释 python 实现 https://www.youtube.com/watch?v=aSbdzpJh8VQ&list=PLqZkRM3t-8wZ3QBcq-xRDjhOzhdM7hW5w&index=14
#
# Dijkstra 寻找从特定起点到图中所有其他节点的路径，使每一条路径的总权重和最小。不管是有向图还是无向图都适用
# 当Dijkstra算法运行完成时，记录下每次找到最短路径时所经过的边，这些边会形成一棵树，称为最短路径树 SPT (shortest path tree)。
# 特性: 这棵树的特性是，树上的任意一个节点到根节点（源点）的路径，就是原图中该节点到源点的最短路径

# SPT: 有Dijkstra算法在图里生成的树, 每个点到原点都是的路径都是最短的路径, 图可以有向可以无向, 权重必须是非负
# MST: 包含原图所有点,无环,且所有边权重和最小, 图必须是无向的, 权重可以为正可以为负也可以全部为1, 全部为1就相当于bfs的过程

# 面试中要掌握Dijkstra和Kruskal(union find)即可


"""
图结构表示 (Graph Structure):
      
          (B)------- 9 -------(D)
         / | \               /   \
        4 11  7            13     2
       /   |   \           /       \
    (A)    |    \        /         (F)
       \   |     \      /          /
        5  |      (E)----------6--
         \ |     /
          (C)---3

边与权重 (Edges & Weights):
- A -> B: 4,  A -> C: 5
- B -> D: 9,  B -> C: 11, B -> E: 7
- C -> E: 3
- D -> E: 13, D -> F: 2
- E -> F: 6
"""

graph = {
    'A': {'B': 4, 'C': 5},
    'B': {'A': 4, 'C': 11, 'D': 9, 'E': 7},
    'C': {'A': 5, 'B': 11, 'E': 3},
    'D': {'B': 9, 'E': 13, 'F': 2},
    'E': {'B': 7, 'C': 3, 'D': 13, 'F': 6},
    'F': {'D': 2, 'E': 6}
}
# 但是很多题目输入是edge list, 需要自己来构建adjacent list 比如:
edges = [
    ['A', 'B', 4], ['A', 'C', 5],
    ['B', 'D', 9], ['B', 'C', 11], ['B', 'E', 7],
    ['C', 'E', 3],
    ['D', 'E', 13], ['D', 'F', 2],
    ['E', 'F', 6]
]

import heapq
from collections import defaultdict
class Solution:
    """
        Dijkstra's Algorithm (Lazy Deletion Version)
        
        TC: O(E log E) - 其中 E 是边数。
            - 每一个边在最坏情况下都会触发一次 heappush。
            - 堆的最大大小可达 E，因此 push/pop 操作为 O(log E)。
            - 渐进意义上 O(E log E) 等价于 O(E log V)。
        
        SC: O(V + E) - 其中 V 是节点数，E 是边数。
            - Adjacency List 存储所有节点和边: O(V + E)。
            - distances 字典存储所有节点距离: O(V)。
            - Priority Queue 在最坏情况下存储所有松弛路径: O(E)。
    """
    def dijkstra(self, edges: list[tuple[str, str, int]], start_node: str, end_node: str):
        # 1 数据预处理, 把edges变成 adjacent list
        graph = defaultdict(dict)
        for u, v, w in edges:
            # 如果edges中不包含来回双向的edge, 就要在图中加两次, 因为给的例子是无向图, 如果给的例子是有向图, 那只需要加一次就行
            # 但是为了保证所有点都在graph里面 有向图时可以写成
            # graph[u][v] = w
            #   if v not in graph: 
            #   graph[v] = {} # 哪怕 只有一条边u->v, 也可以保证v会在graph里出现
            graph[u][v] = w
            graph[v][u] = w

        # 2 初始化
        # pq 存储格式: (当前累计距离, 当前节点)
        # 使用优先队列（最小堆）确保每次弹出的都是路径最短的点
        pq = [(0, start_node)]

        # min_dist 记录从起点到每个节点的最短距离
        # 初始状态：起点为 0，其他所有点为无穷大
        min_dist = {node: float('inf') for node in graph} # for node in graph = for node in graph.keys()
        min_dist[start_node] = 0

        # predecessors 记录每个节点的最佳前驱
        predecessors = {node: None for node in graph}

        # 3 算法核心循环
        while pq:
            # 弹出当前距离起点最近的节点
            cur_dist, cur_node = heapq.heappop(pq)

            if cur_node == end_node:
                return cur_dist, self._reconstruct_path(predecessors, end_node)

            # 如果当前点已经处理过，直接跳过（惰性删除）
            if cur_dist > min_dist[cur_node]:
                continue
            
            for nb, w in graph[cur_node].items():
                new_dist = cur_dist + w

                if new_dist < min_dist[nb]: # 必须要更小的才可以入pq，相当的都不可以入, 不然会重复的循环处理weight为0的两边的node
                    min_dist[nb] = new_dist
                    predecessors[nb] = cur_node
                    heapq.heappush(pq, (new_dist, nb))

        return -1, []

    def _reconstruct_path(self, predecessors: dict, end: str) -> list[str]:
        """
        从终点逆向回溯到起点
        TC: O(V)
        SC: O(V)
        """
        path = []
        cur = end
        while cur is not None:
            path.append(cur)
            cur = predecessors[cur]
        
        # 因为是从终点往回找的，最后需要翻转
        return path[::-1] 
                
def run_tests():
    sol = Solution()
    
    # Test Case 1: 你提供的示例图片 (A -> F)
    # 预期结果: 14 (路径: A-C-E-F 为 5+3+6=14)
    edges1 = [
        ['A', 'B', 4], ['A', 'C', 5],
        ['B', 'D', 9], ['B', 'C', 11], ['B', 'E', 7],
        ['C', 'E', 3],
        ['D', 'E', 13], ['D', 'F', 2],
        ['E', 'F', 6]
    ]
    print(f"Test 1 (Example Graph): {sol.dijkstra(edges1, 'A', 'F')} (Expected: 14)")

    # Test Case 2: 权重优先 (直达虽快但贵)
    # 预期结果: 2 (路径: A-C-B 为 1+1=2，虽然 A-B 直接连通但权重是 10)
    edges2 = [['A', 'B', 10], ['A', 'C', 1], ['C', 'B', 1]]
    print(f"Test 2 (Weight Priority): {sol.dijkstra(edges2, 'A', 'B')} (Expected: 2)")

    # Test Case 3: 图不连通 (孤立点)
    # 预期结果: -1
    edges3 = [['A', 'B', 1], ['C', 'D', 1]]
    print(f"Test 3 (Disconnected): {sol.dijkstra(edges3, 'A', 'D')} (Expected: -1)")

    # Test Case 4: 起点和终点相同
    # 预期结果: 0
    edges4 = [['A', 'B', 5]]
    print(f"Test 4 (Start == End): {sol.dijkstra(edges4, 'A', 'A')} (Expected: 0)")

    # Test Case 5: 存在环路
    # 预期结果: 3 (路径: A-B-C 为 1+2=3)
    edges5 = [['A', 'B', 1], ['B', 'C', 2], ['C', 'A', 5]]
    print(f"Test 5 (Cycle): {sol.dijkstra(edges5, 'A', 'C')} (Expected: 3)")


    # Test Case 6: 包含 0 权重边
    # A --(0)-- B --(5)-- C
    # 预期结果: 5 (A 到 C 的距离)
    edges6 = [['A', 'B', 0], ['B', 'C', 5]]
    print(f"Test 6 (Zero Weight): {sol.dijkstra(edges6, 'A', 'C')} (Expected: 5)")

    # Test Case 7: 0 权重环
    # A --(0)-- B, B --(0)-- A
    edges7 = [['A', 'B', 0]]
    print(f"Test 7 (Zero Weight Cycle): {sol.dijkstra(edges7, 'A', 'B')} (Expected: 0)")

run_tests()
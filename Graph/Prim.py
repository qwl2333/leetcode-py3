import heapq
from collections import defaultdict

# TC: 在最坏情况下（比如完全图），每一条边都会被 heappush 进堆一次。
# 堆中最多会有 E 条边，因此每次 heappush 和 heappop 的复杂度为 
# O(logE)。总共有 E 次堆操作，所以总复杂度为 O(ElogE)。

# SC: O(V + E)
#         - 邻接表 (graph): 存储所有的点和边, 空间为 O(V + E)
#         - 访问集合 (visited): 存储所有顶点, 空间为 O(V)
#         - 优先队列 (min_heap): 最坏情况下存储所有边, 空间为 O(E)
#         - 结果集 (mst): 存储生成树的边, 空间为 O(V), 因为最小生成树一点是有V-1条边

def prim(edges):
    # 构建邻接表
    graph = defaultdict(list)
    nodes = set()
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
        nodes.add(u)
        nodes.add(v)
    
    visited = set() # 当前已经在最小生成树（MST）里的点
    mst = []
    total_weight = 0
    min_heap = []

    # 和 bfs 类似, 需要一个起点, 而且要加到visited和min_heap里面
    # 任意选一个起点, 这里选的是edges[0][0]
    start = edges[0][0]
    visited.add(start)
    for weight, end in graph[start]:
        heapq.heappush(min_heap, (weight, start, end))
    
    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if v in visited: # v已经被visited过了, 上面一行被pop出来的边会形成环, 需要跳过
            continue

        visited.add(v)
        mst.append((u, v, weight))
        total_weight += weight
        if len(mst) == len(nodes) - 1:
            return mst, total_weight
        for nb_weight, nb in graph[v]:
            if nb not in visited:
                heapq.heappush(min_heap, (nb_weight, v, nb))
    
    return [], -1

# pylint: disable=pointless-string-statement
r"""
图结构表示 (Graph Structure):

          (B)------- 4 -------(D)------- 3 -----(F)
           |  \               /  \             /
           |    1            /    2           /   
           2      \         5      \         4
           |        \      /        \       /
           |          \   /          \     /
          (A)----- 3 --(C)----- 6 -----(E)/

边与权重 (Edges & Weights):
- A <-> B: 2,  A <-> C: 3
- B <-> C: 1,  B <-> D: 4
- C <-> D: 5,  C <-> E: 6
- D <-> E: 2,  D <-> F: 3
- E <-> F: 4
"""

edges = [
    ("A", "B", 2),
    ("A", "C", 3),
    ("B", "C", 1),
    ("B", "D", 4),
    ("C", "D", 5),
    ("C", "E", 6),
    ("D", "E", 2),
    ("D", "F", 3),
    ("E", "F", 4),
]
mst, total = prim(edges)

print('Edges in MST')
for u, v, w in mst:
    print(f'{u} - {v}: {w}')

print(f'Total weight: {total}')
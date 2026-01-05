# 想得到无向加权联通图的Minimum Spanning Tree使用这个算法, 比如城市之间铺电缆, 为了使所有城市都联通且总花费最少的问题
# Minimum Spanning Tree (MST) 的中文是最小生成树。它指在一个连通的加权无向图中，选出一些边连接所有顶点，形成一棵树，且所有选出边的权值总和最小。
# 在计算机科学和网络设计中，它用于优化网络连接、降低成本，通常用 Prim算法 和 Kruskal算法 解决。
# 生成树 (Spanning Tree)：一个图的生成树是包含原图所有顶点、且没有回路的子图，对于有 n 个顶点的图，生成树有 n-1 条边。
# 加权图 (Weighted Graph)：图中的边都有一个关联的数字（权重），通常代表成本、距离等。
# 最小生成树 (MST)：在所有可能的生成树中，总权重（边权重之和）最小的那棵树。

# prim mst 算法解释 python实现 https://www.youtube.com/watch?v=rS6_LTsvx7w
# kruskal mst 算法解释 python实现 https://www.youtube.com/watch?v=ZsLlhezMxiM&list=PLqZkRM3t-8wZ3QBcq-xRDjhOzhdM7hW5w&index=10&pp=iAQB

# 在使用kruskal前,必须了解union_find_basic.py 和 union_find.py 知道加了path compression和秩ranks后 find和union的tc 已经接近O(1)
class UnionFind:
    def __init__(self, N: int):
        self.parents = list(range(N)) # [i for i in range(N)] 也可以
        self.ranks = [1 for _ in range(N)]

    # recursion
    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        else:
            # return self.find(self.parents[x])

            # path compression
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    # iterative
    '''
    The time complexity of the Find operation, when using path compression, 
    is nearly constant and is bounded by O(α(n)), 
    where α(n) is the inverse Ackermann function. For all practical purposes, 
    this grows extremely slowly, and even for very large inputs, it can be considered as close to constant time.
    '''
    def findIterative(self, x: int) -> int:
        root = x
        # find the root node of x
        while root != self.parents[root]:
            root = self.parents[root]
        
        # path compression: make all ancestors point directly to root
        while x != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        
        return root
    
    '''
    The time complexity of the Union operation, when using union by rank or size, is also O(α(n)) because the depth of any tree is limited by the inverse Ackermann function.
    '''
    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y: # 不能merge 两个集合，因为有环
           return False
        else:
            # 把个子矮的树挂在个之高的树下面,避免树越来越深, ranks[x] 代表了x为根的树的高度
            if self.ranks[root_x] > self.ranks[root_y]:
                self.parents[root_y] = root_x
            elif self.ranks[root_x] < self.ranks[root_y]:
                self.parents[root_x] = root_y
            else:
                self.parents[root_x] = root_y
                self.ranks[root_y] += 1
            return True

class Solution:
    def krustal(self, indexed_edges, num_nodes):
        '''
        仅处理整数节点的krustal实现, 返回index形式的mst
        '''
        uf = UnionFind(num_nodes)
        indexed_edges.sort()
        mst = []
        total_weight = 0

        for weight, u, v in indexed_edges:
            if uf.union(u, v):
                mst.append((u, v, weight))
                total_weight += weight
            if len(mst) == num_nodes - 1:
                break
        
        return mst, total_weight
    
    def prepare_indexed_graph(self, edges):
        '''
        输入形如(weight, str_node_u, str_node_v)的边列表
        输出索引化的边, 节点数, 字符串 <-> 索引映射
        '''
        nodes = set()
        for _, u, v in edges:
            nodes.add(u)
            nodes.add(v)
        
        node_to_index = {node: idx for idx, node in enumerate(sorted(nodes))}
        index_to_node = {idx: node for node, idx in node_to_index.items()}
        indexed_edges = [(w, node_to_index[u], node_to_index[v]) for w, u, v in edges]

        return indexed_edges, len(nodes), node_to_index, index_to_node

    def restore_mst_labels(self, mst_indexed, index_to_node):
        '''
        将mst从索引形式转换为字符串形式
        '''
        return [(index_to_node[u], index_to_node[v], w) for u, v, w in mst_indexed]

s = Solution()
edges = [
    (7, 'A', 'B'),
    (1, 'A', 'C'),
    (5, 'B', 'C'),
    (6, 'B', 'D'),
    (3, 'C', 'D'),
    (4, 'C', 'E'),
    (2, 'D', 'E')
]

indexed_edges, num_nodes, node_to_index, index_to_node = s.prepare_indexed_graph(edges)
mst_indexed, total = s.krustal(indexed_edges, num_nodes)
mst_labeled = s.restore_mst_labels(mst_indexed, index_to_node)

# 输出结果
print('MST edges:')
for u, v, w in mst_labeled:
    print(f'{u} - {v} (weight: {w})')
print(f'Total weight: {total}')

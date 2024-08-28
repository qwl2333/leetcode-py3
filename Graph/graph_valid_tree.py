# lc 261
from collections import deque
class Solution:
    # 无相图是否有环 Time， space O(n + e) = O(n) 因为是树，edge = num of vertex - 1
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        graph = {i:[] for i in range(n)}
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)
        
        visited = set()
        def has_cycle(prev: int, cur: int) -> bool: # 其实查看的是从prev到cur，是不是包含在一个环里面的边
            if cur in visited:
                return True

            visited.add(cur)
            for nb in graph[cur]:
                if nb == prev:
                    continue
                if has_cycle(cur, nb):
                    return True
                
            return False
        
        return not has_cycle(-1, 0) and len(visited) == n # len(visited) == n means all nodes are connected

    def validTreeBFS(self, n: int, edges: list[list[int]]) -> bool:
        graph = {i: [] for i in range(n)}
        for s, e in edges:
            graph[s].append(e)
            graph[e].append(s)

        q = deque([(0, -1)])
        visited = set([0])
        while q:
            cur, parent = q.popleft()
            for nb in graph[cur]:
                if nb == parent:
                    continue
                if nb in visited:
                    return False
                visited.add(nb)
                q.append((nb, cur))

        return len(visited) == n

    def validTreeUnionFind(self, n: int, edges: list[list[int]]) -> bool:
        parents = [i for i in range(n)]
        num_of_components = n

        def find_parent(parents: list[int], i): # time O(n) n - number of nodes
            if parents[i] == i:
                return i
            else:
                return find_parent(parents, parents[i])
        
        for e in edges:
            p1 = find_parent(parents, e[0])
            p2 = find_parent(parents, e[1])
            if p1 != p2: # 可以用来找环，p1 == p2 证明有环
                parents[p1] = p2
                num_of_components -= 1
            else:
                return False

        return num_of_components == 1
    

from collections import deque
class UnionFind:
    def __init__(self, N: int):
        self.parents = list(range(N)) # [i for i in range(N)] 也可以

    def find(self, x: int) -> int:
        if self.parents[x] == x:
            return x
        else:
            return self.find(self.parents[x])
            # path compression
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x: int, y: int):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y: # 不能merge 两个集合，因为有环
           return False
        else:
            self.parents[root_x] = root_y
            return True

class SolutionUsingUnionFindClass:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        union_find = UnionFind(n)
        
        for s, e in edges:
            if not union_find.union(s, e):
                return False

        return True

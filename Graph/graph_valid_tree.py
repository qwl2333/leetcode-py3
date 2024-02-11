# lc 261
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

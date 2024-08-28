# lc 207
from collections import deque
class Solution:
    # BFS topological sort, time O(V + E) Vertex - numCourses, Edges - len(prerequisites), space O(V + E) because of adjacent list we created
    # Because we have to visit every vertex and every edge once
    # 有向图有没有环，可以用拓扑排序
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        indegree = [0 for _ in range(numCourses)]
        edges = [[] for _ in range(numCourses)]
        for end, start in prerequisites:
            indegree[end] += 1
            edges[start].append(end)
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        count = 0 # count how many course are popped out from queue, ideally if no cycle, all courses would be popped out
        while queue:
            cur = queue.popleft()
            count += 1
            for nb in edges[cur]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    queue.append(nb)
        
        return count == numCourses

    # DFS + memo, same time and space as BFS
    def canFinishDFS(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        pre_map = {i:[] for i in range(numCourses)} # int, list[int]
        for a, b in prerequisites:
            pre_map[a].append(b)
        cache = [-1 for i in range(numCourses)] # -1 means dfs还没经过这个课程， 1表示可以finish，-1表示不能finish，但是此题用不到-1，因为dfs遇到false就结束了

        visited = set() # 回溯式记录dfs路径上所有经过的点
        def dfs(cur_course: int) -> bool: # dfs function 意思是以cur_course为起点，能否顺利完成所有prereq课程
            if pre_map[cur_course] == []:
                cache[cur_course] = 1
                return True
            if cur_course in visited:
                # cache[cur_course] = -1
                return False

            if cache[cur_course] != -1:
                return cache[cur_course] == 1

            visited.add(cur_course)
            for nb in pre_map[cur_course]:
                if not dfs(nb):
                    # cache[cur_course] = -1
                    return False
            visited.remove(cur_course)
            cache[cur_course] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True


s = Solution()
print(s.canFinish(2, [[1, 0]]))
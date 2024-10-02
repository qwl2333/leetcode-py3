# lc 1778 类似 lc 489
# https://leetcode.com/problems/shortest-path-in-a-hidden-grid/solutions/1100020/python-dsf-to-explore-the-graph-and-bfs-to-find-minimum-distance/
import collections

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:

        # first use dfs to find all possible reachable positions
        dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        anti = {"U": "D", "D": "U", "L": "R", "R": "L"}

        isValid = {}
        isValid[(0, 0)] = master.isTarget()  # Acts as visited set

        def dfs(r, c):
            for d in dirs:
                dr, dc = dirs[d]
                nr, nc = r + dr, c + dc
                if (nr, nc) not in isValid and master.canMove(d):
                    # move forward
                    master.move(d)
                    isValid[(nr, nc)] = master.isTarget()
                    dfs(nr, nc)
                    # move back
                    master.move(anti[d])

        dfs(0, 0)

        # now use bfs to find the minimum distance
        q = collections.deque([(0, 0)])  # (r, c, step)
        seen = set()
        steps = 0

        while q:
            size = len(q)
            for i in range(size):
                r, c = q.popleft()

                for d in dirs:
                    dr, dc = dirs[d]
                    nr, nc = r + dr, c + dc
                    if (nr, nc) in isValid and (nr, nc) not in seen:
                        if isValid[(nr, nc)] == True:
                            return steps + 1
                        seen.add((nr, nc))
                        q.append((nr, nc))
            steps += 1

        return -1
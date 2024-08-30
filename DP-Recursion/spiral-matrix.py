# lc 54
class Solution:
    # time O(n * m), space O(n * m) 考虑到返回到list，如果不考虑返回到list，最好可以到O(1), 通过尾递归调用和优化掉visited
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        visited = set() # 这个可以用改变matrix值来优化掉
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.res = []

        def spiral_traverse(i, j, dirs, idx):
            self.res.append(matrix[i][j])
            visited.add((i, j))
            if len(visited) == n * m:
                return

            newi = i + dirs[idx][0]
            newj = j + dirs[idx][1]
            if ((newi, newj) in visited
                or newi == n or newj == m
                or newi == -1 or newj == -1):
                idx = (idx + 1) % 4 # 可以保证idx永远在0,1,2,3,0,1,2,3...循环
                newi = i + dirs[idx][0]
                newj = j + dirs[idx][1]

            spiral_traverse(newi, newj, dirs, idx)
            # a recursive function written to take advantage of tail-call optimization can use constant stack space.

        spiral_traverse(0, 0, directions, 0)
        return self.res

# lc 733
from collections import deque
from typing import List
class Solution:
    # BFS time O(m * n) m - # of row, n - # of col, space O(m * n) - 一般dfs和bfs的时间空间是一样的，考虑栈的情况下，都是所有节点数
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        if image[sr][sc] == color:
            return image
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        old_color = image[sr][sc]
        queue = deque([(sr, sc)])
        visited = set([(sr, sc)]) # 也可以不要set，用颜色改没改来判断是否visited
        image[sr][sc] = color
        while queue:
            cur = queue.popleft()
            for dir in directions:
                new_r = cur[0] + dir[0]
                new_c = cur[1] + dir[1]
                if (
                    new_r >= 0 and new_r < len(image) 
                    and new_c >= 0 and new_c < len(image[0])
                    and image[new_r][new_c] == old_color 
                    and (new_r, new_c) not in visited
                ):
                    image[new_r][new_c] = color
                    visited.add((new_r, new_c))
                    queue.append((new_r, new_c))
        
        return image

    # DFS time O(m * n)  space O(m * n)
    def floodFillDFS(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        old_color = image[sr][sc]
        def dfs(image: List[List[int]], sr: int, sc: int, new_color: int, old_color: int):
            if (sr < 0 or sr > len(image) - 1 
            or sc < 0 or sc > len(image[0]) - 1 
            or image[sr][sc] != old_color): 
                return

            if image[sr][sc] == color: # visited
                return

            image[sr][sc] = color
            dfs(image, sr, sc - 1, new_color, old_color)
            dfs(image, sr, sc + 1, new_color, old_color)
            dfs(image, sr - 1, sc, new_color, old_color)
            dfs(image, sr + 1, sc, new_color, old_color)
        
        dfs(image, sr, sc, color, old_color)
        return image

            
s = Solution()

print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

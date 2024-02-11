class Solution:
    # Time O(n * m * dfs) dfs = 4^len(word)
    # 此题不可以用cache，光靠r，c，count不能判断这个点是不是一定在最后的path里
    # 比如 
    #   [A B‘ E]
    #   [B C D]
    # 目标ABCDEB, 对E来说，它既可以在ABCDEB的第4位置，也可以在AB'CDE的第四位置，后者是无解的，返回false，会导致正确的路径后来经过E时
    # 由于cache的value认为此处不能走了

    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        n = len(board)
        m = len(board[0])

        def dfs(r: int, c: int, count: int) -> bool:
            if count == len(word) - 1:
                return True
            
            count += 1
            visited.add((r, c))
            print(count)
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if 0 <= new_r < n and 0 <= new_c < m and board[new_r][new_c] == word[count] and (new_r, new_c) not in visited:
                    if dfs(new_r, new_c, count):
                        return True
            count -= 1
            visited.remove((r, c))
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = set()
                    if dfs(i, j, 0):
                        return True
        
        return False

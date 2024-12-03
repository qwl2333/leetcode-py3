# lc 79
class Solution:
    # Time O(n * m * dfs) dfs = 3^len(word)
    '''
Complexity Analysis
Time Complexity: O(N⋅3^L) where N is the number of cells in the board and L is the length of the word to be matched.

For the backtracking function, initially we could have at most 4 directions to explore, but further the choices are reduced into 3 (since we won't go back to where we come from).
As a result, the execution trace after the first step could be visualized as a 3-nary tree, each of the branches represent a potential exploration in the corresponding direction. Therefore, in the worst case, the total number of invocation would be the number of nodes in a full 3-nary tree, which is about 3^L.

We iterate through the board for backtracking, i.e. there could be N times invocation for the backtracking function in the worst case.

As a result, overall the time complexity of the algorithm would be O(N⋅3^L).

Space Complexity: O(L) where L is the length of the word to be matched.

The main consumption of the memory lies in the recursion call of the backtracking function. The maximum length of the call stack would be the length of the word. Therefore, the space complexity of the algorithm is O(L)

这是editorial的空间复杂度，它用了标记board，避免了用visited的set来记录，实际我的解法应该是o(len(word) + n * m) worst case visited 会包含所有nodes，所以需要n * m

    '''
    # 此题不可以用cache，光靠r，c，count不能判断这个点是不是一定在最后的path里
    # 比如 
    #   [A B‘ E]
    #   [B C D]
    # 目标ABCDEB, 对E来说，它既可以在ABCDEB的第4位置，也可以在AB'CDE的第四位置，后者是无解的，返回false，会导致正确的路径后来经过E时
    # 由于cache的value认为此处不能走了

    def exist(self, board: list[list[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs_helper(x: int, y: int, index: int, visited: set) -> bool:            
            if word[index] != board[x][y]:
                return False
            
            if index == len(word) - 1:
                return True

            for dx, dy in directions:
                newx = x + dx
                newy = y + dy
                if 0 <= newx < n and 0 <= newy < m and (newx, newy) not in visited:
                    visited.add((newx, newy)) # 可能是一个潜在的路
                    if dfs_helper(newx, newy, index + 1, visited):
                        return True
                    visited.remove((newx, newy)) # 返回了false说明(newx, newy)不通到最后, 去掉它
            
            return False
        
        for i in range(n):
            for j in range(m):
                if dfs_helper(i, j, 0, set([(i, j)])):
                    return True
        
        return False

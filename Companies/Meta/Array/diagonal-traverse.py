# lc 498
# https://leetcode.com/problems/diagonal-traverse/solutions/97711/java-15-lines-without-using-boolean/
from collections import defaultdict
class Solution:
    '''
    这个解法空间复杂度高因为用了groups, 但是很好理解, 面试可以用这个解法
    时间复杂度: O(m * n)。矩阵中每个元素只被访问一次，并被添加到 defaultdict 一次，最后被添加到 result 一次。这是最优的时间复杂度。空间复杂度: O(m * n)。用于存储 groups 字典。
    '''
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat or not mat[0]:
            return []

        M = len(mat)    # 行数
        N = len(mat[0]) # 列数
        
        # 使用 defaultdict(list) 来存储每一条对角线上的元素
        # 键 k = i + j
        groups = defaultdict(list)
        
        # 步骤 1: 遍历矩阵并进行分组
        for r in range(M):
            for c in range(N):
                # 将元素添加到以索引和 (r + c) 为键的列表中
                groups[r + c].append(mat[r][c])
                
        # 步骤 2: 遍历字典并按方向处理
        result = []
        
        # 对角线总数是 M + N - 1，索引和 k 从 0 到 M + N - 2
        max_sum = M + N - 2
        
        for k in range(max_sum + 1):
            
            # 获取当前对角线的所有元素
            current_diagonal = groups[k]
            
            # k 是偶数：需要向上/右遍历 (元素顺序是向下的，所以要反转)
            if k % 2 == 0:
                # Python 的 list.reverse() 是原地反转，也可以使用 current_diagonal[::-1] 
                # 这里的目的是模拟 '向上' 的遍历顺序。
                current_diagonal.reverse()
                result.extend(current_diagonal)
            
            # k 是奇数：需要向下/左遍历 (元素顺序已经是向上的，所以保持不变)
            else:
                result.extend(current_diagonal)
                
        return result

    # 优化空间复杂度 不算返回的数组为O(1)
    def findDiagonalOrder1(self, mat: list[list[int]]) -> list[int]:
        n = len(mat)
        m = len(mat[0])
        r, c = 0, 0
        res = [0 for _ in range(n * m)]
        for i in range(n * m):
            res[i] = mat[r][c]
            if (r + c) % 2 == 0: # move right up
                if c == m - 1: # 顺序不可调换，必须先check c有没有到最右,如果先check r, 在增加c时，有可能c已经到最右了c就出界了
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else: # move left down
                if r == n - 1: # 同理如果先check c==0 可能会出现r出界的情况
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return res

s = Solution()
print(s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
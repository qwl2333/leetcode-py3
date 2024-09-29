# lc 269
from collections import deque
class Solution:
    # t O(n) s O(n) n - total number of characters in words
    '''
    输出的结果必须包含所有在words里面出现过的characters, 比如 'abc', 'def'
    输出的结果可以是'abcdef', 只要a出现在d之前
    所以, queue里面必须包含所有的入度为0的点, 就算是bc, ef这种没有边的也要放进去
    这也是为什么在build graph一开始要把所有的char都放进indgree里面并设置初始值为0
    '''
    def alienOrder(self, words: list[str]) -> str:
        '''
         wrt, wrf
         t -> f
         indegree[f] += 1
         char_graph[t].add(f)
        '''
        indegree = {}
        char_graph = {} # char, set()
        n = len(words)

        # Build the graph
        for word in words:
            for c in word:
                if c not in indegree:
                    indegree[c] = 0
                    char_graph[c] = set() # 因为必须把所有char放到indegree里面,所以顺便可以initialize graph, 当然你省略这一行直接用defaultdict(set)也行

        for i in range(1, n):
            first = words[i - 1]
            second = words[i]
            length = min(len(first), len(second))
            for j in range(length):
                if first[j] != second[j]: # 这里为什么要先check first[j] != second[j], 因为只要不等就必须break了, 后面的不需要遍历了
                                          # 但是不等的这一对chars可能之前已经加进去graph里面了, 所以要在graph里面先确认没加过才可以
                                          # 加进graph, 同时修改indegree
                    if second[j] not in char_graph[first[j]]:
                        char_graph[first[j]].add(second[j])
                        indegree[second[j]] += 1

                    break
                if j == length - 1 and len(first) > len(second): # 如果在最后一个字符还是相同的, 但是first比second长
                                                                 # 那就是'abc', 'ab'的情况, 这种不是一个valid的lexicographic order
                    return ''

        # Topo sort
        q = deque()
        res = ''
        for char, indgr in indegree.items():
            if indgr == 0:
                q.append(char)
        while q:
            cur = q.popleft()
            res += cur
            for nb in char_graph[cur]:
                indegree[nb] -= 1
                if indegree[nb] == 0:
                    q.append(nb)
        
        return res if len(res) == len(indegree) else "" # 最后要确认res结果包含了所有出现过的chars
                
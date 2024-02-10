# lc 721
class Solution:
    # time O(v + e) v: 节点数应该是 len(accounts) + # of unique email address, e: 边数应该是总共的# of email address
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # 每个account都是一个数字节点， start from 0
        # 同时每一个email也是一个节点，如果有相同的email，证明通过这个相同的email，两个数字节点相通了
        graph = {}
        for i in range(len(accounts)):
            length = len(accounts[i])
            for j in range(1, length):
                email = accounts[i][j]
                if email not in graph:
                    graph[email] = []
                graph[email].append(i)
        
        visited = [False for _ in range(len(accounts))]
        
        def dfs(i: int, emails: set):
            if visited[i]:
                return

            visited[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for node in graph[email]:
                    if not visited[node]:
                        dfs(node, emails)

        res = []
        for i in range(len(accounts)):
            if not visited[i]:
                emails = set()
                dfs(i, emails)
                res.append([accounts[i][0]] + sorted(emails))

        return res

    # 也可以利用union find数据结构来做


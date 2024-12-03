# lc 721
from collections import defaultdict
class Solution:
    # time O(v + e) v: 节点数应该是 len(accounts) + # of unique email address, e: 边数应该是总共的# of email address
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # 每个account都是一个节点， start from 0
        # 同时每一个email也是一个节点，如果有相同的email，证明通过这个相同的email，两个数字节点相通了
        # 此时所有的account点和email点组成了一个图
        # account 可以直接找到email的邻居 因为accounts里面有
        # 但是email的account邻居需要先构建出来
        email_to_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_to_accounts[email].append(i)

        visited_accounts = set()
        def find_emails_connected_to_account(account_idx: int, emails_found: set):
            visited_accounts.add(account_idx)
            cur_account = accounts[account_idx]
            for i in range(1, len(cur_account)):
                email = cur_account[i]
                if email in emails_found:
                    continue
                emails_found.add(email)
                for nb_account in email_to_accounts[email]:
                    if nb_account not in visited_accounts:
                        find_emails_connected_to_account(nb_account, emails_found)
        
        res = []
        for i, account in enumerate(accounts):
            if i in visited_accounts:
                continue
            emails = set()
            find_emails_connected_to_account(i, emails)
            res.append([account[0]] + sorted(emails))
        
        return res

    # 也可以利用union find数据结构来做
    # Time O((n + e) * a(n)) n - number of accounts, e - number of emails
    def accountsMergeUnionFind(self, accounts: list[list[str]]) -> list[list[str]]:
        email_to_account = {}
        uf = UnionFind(len(accounts))
        for account_id, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                if email not in email_to_account:
                    email_to_account[email] = account_id
                else:
                    uf.union(account_id, email_to_account[email])

        group_by_account = defaultdict(list)
        for email, account_id in email_to_account.items():
            main_account = uf.find(account_id)
            group_by_account[main_account].append(email)
        
        res = []
        for main_account_id, emails in group_by_account.items():
            name = accounts[main_account_id][0]
            data = [name]
            data.extend(sorted(emails))
            res.append(data)
        return res

class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.ranks = [1] * size

    def find(self, x):
        root = x
        while root != self.parents[root]:
            root = self.parents[root]
        
        while x != root:
            parent = self.parents[x]
            self.parents[x] = root
            x = parent
        
        return root
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.ranks[root_x] > self.ranks[root_y]:
                self.parents[root_y] = root_x
            elif self.ranks[root_x] < self.ranks[root_y]:
                self.parents[root_x] = root_y
            else:
                self.parents[root_x] = root_y
                self.ranks[root_y] += 1
        
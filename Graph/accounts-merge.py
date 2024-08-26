# lc 721
from collections import defaultdict
class Solution:
    # time O(v + e) v: 节点数应该是 len(accounts) + # of unique email address, e: 边数应该是总共的# of email address
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        # 每个account都是一个数字节点， start from 0
        # 同时每一个email也是一个节点，如果有相同的email，证明通过这个相同的email，两个数字节点相通了
        email_to_accounts = defaultdict(list)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]
                email_to_accounts[email].append(i)

        visited_accounts = set()
        def find_emails_connected_to_account(account_idx: int, emails_found: set):
            if account_idx in visited_accounts:
                return
            visited_accounts.add(account_idx)
            cur_account = accounts[account_idx]
            for i in range(1, len(cur_account)):
                email = cur_account[i]
                if email in emails_found:
                    continue
                emails_found.add(email)
                for nb_account in email_to_accounts[email]:
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


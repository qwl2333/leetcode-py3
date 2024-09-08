'''
https://www.1point3acres.com/bbs/thread-1063667-1-1.html
背景： 假设现在有一个store 用户信用分数的system， 对于一个用户，分别有FICO 和 VIGA（记不得名字了）两种信用分，给一个n 就是最大可以存的history 的数量

题目：实现两个function
insert credit history
存取用户信息
get credit history （x， id，creditType）
返回该用户最近的 X 个信用分 对于相对应的 credittype （FICO/ VIGA）
'''
from collections import deque

class ScoreNode:
    def __init__(self, user_id: int, scores: int, type: str):
        self.user_id = user_id
        self.scores = scores
        self.type = type

class CreditHistorySystem:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.history = deque()
        self.users = {}
    
    def insert_credit(self, user_id: int, scores: int, type: str):
        new_score = ScoreNode(user_id, scores, type)
        self.history.append(new_score)
        if user_id not in self.users:
            self.users[user_id] = {'F': deque(), 'V': deque()}
        self.users[user_id][type].append(new_score)
        
        if len(self.history) > self.capacity:
            score_to_evict = self.history.popleft()
            old_user_id = score_to_evict.user_id
            old_type = score_to_evict.type
            self.users[old_user_id][old_type].popleft()
    
    def get_credits(self, user_id: int, number: int, type: str):
        for i in range(1, number + 1):
            print(self.users[user_id][type][-i].scores)

system = CreditHistorySystem(4)
system.insert_credit(1, 10, 'F')
system.insert_credit(1, 20, 'F')
system.insert_credit(1, 30, 'F')
system.insert_credit(1, 40, 'F')
system.insert_credit(1, 50, 'F')
system.insert_credit(2, 60, 'F')
system.get_credits(2, 1, 'F')

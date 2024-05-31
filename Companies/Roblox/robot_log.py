# 和 lc 362 design hit counter很像
from collections import deque
class RobotLog:
    def __init__(self, window_size: int, threshold: int) -> None:
        if window_size <= 0 or threshold <= 0:
            raise ValueError('window_size and threshold must be bigger than 0')

        self.window_size = window_size
        self.threshold = threshold
        self.time_ip = deque()
        self.ip_freq = {}
        self.bot_ips = set()

    # use unix timestamp
    def find_robot_ips(self):
        with open('Companies/Roblox/logs.txt', 'r') as file:
            content = file.read()
        lines = content.splitlines()
        freq = {}
        res = set()
        for line in lines:
            _timestamp, id = line.strip().split(',')
            freq[id] = freq.get(id, 0) + 1
            if freq[id] >= self.threshold:
                res.add(id)
        return res

    # return bots in (timestamp - ,timestamp]
    def get_bots(self, timestamp: int, ip: str) -> list[str]:
        '''
            1. need a deque [timestamp, ip]
                need a map ip: count
                need a set for bot ip
            2. add new [timestamp, ip] to the deque, then popleft for all timestamp <= cur timestamp - window_size
                update map ip: count while insert and popleft from deque
                update set while updating map ip: count
                return set
        '''
        self.time_ip.append([timestamp, ip])
        self.ip_freq[ip] = self.ip_freq.get(ip, 0) + 1
        if self.ip_freq[ip] >= self.threshold:
            self.bot_ips.add(ip)
        
        while self.time_ip and self.time_ip[0][0] <= timestamp - self.window_size:
            _ts, stale_ip = self.time_ip.popleft()
            self.ip_freq[stale_ip] -= 1
            if self.ip_freq[stale_ip] < self.threshold and stale_ip in self.bot_ips:
                self.bot_ips.remove(stale_ip)
        print(f'ip_freq: {self.ip_freq}')
        return list(self.bot_ips)



s = RobotLog(3, 1)
print(s.find_robot_ips())
print('---------------------')
print(s.get_bots(1, 'ip1'))
print(s.get_bots(2, 'ip2'))
print(s.get_bots(3, 'ip3'))
print(s.get_bots(4, 'ip3'))
print(s.get_bots(4, 'ip2'))
print(s.get_bots(5, 'ip2'))

# cornor case: 最后和考官明确 threshold > 0 window_size > 0
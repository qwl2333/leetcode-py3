# lc 636
class Solution:
    # T: O(n) n - len of logs, S: O(n)
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0 for i in range(n)]
        stack = []
        for log in logs:
            id, operation, cur_time = log.split(':')
            id, cur_time = int(id), int(cur_time)
            if operation == 'start':
                stack.append((id, cur_time))
            else: # operation == 'end'
                _id, cur_start_time = stack.pop()
                time_taken = cur_time - cur_start_time + 1
                res[id] += time_taken

                if stack:
                    caller_id, _caller_start_time = stack[-1]
                    res[caller_id] -= time_taken
        
        return res

s = Solution()
print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
# lc 636
class Solution:
    # T: O(n), S: O(n)
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        res = [0] * n
        stack = []           # 存当前在跑的函数 id
        prev_time = 0        # 上一个时间点

        for log in logs:
            fid, typ, t = log.split(':')
            fid, t = int(fid), int(t)

            if typ == 'start':
                if stack:
                    # 从 prev_time 到 t-1 都是栈顶在跑
                    res[stack[-1]] += t - prev_time
                stack.append(fid)
                prev_time = t
            else:  # 'end'
                # 栈顶函数从 prev_time 跑到 t
                res[stack[-1]] += t - prev_time + 1
                stack.pop()
                prev_time = t + 1  # 这些+1包括前面21行的+1 本质上 
                                   # 开始的时间start 5，和end 5其实不是一个时间
                                   # end 5 代表的是 start 6，看leetcode 例子的图片就知道了

        return res

s = Solution()
print(s.exclusiveTime(2, ["0:start:0","1:start:2","1:end:5","0:end:6"]))
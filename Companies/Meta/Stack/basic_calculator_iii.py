# lc 772
from collections import deque
class Solution:
    '''
    利用 反复调用 227 basic calculator ii的解法来解
    会发现time O(n^2)
    思考如何优化, 最好是在找()时做优化, 想到了用deque来装input s, 
    当遇到 ( 时就不用费心去找 ) 了
    '''
    def calculate(self, s: str) -> int:
        stack = []
        cur_num = 0
        prev_op = '+'
        s = s + '+'
        idx = 0
        while idx < len(s):
            c = s[idx]
            if c == ' ':
                continue
            if c.isdigit():
                cur_num = cur_num * 10 + int(c)
            elif c == '(':
                close_idx = idx + 1
                left = 1
                while left != 0:
                    if s[close_idx] == '(':
                        left += 1
                    if s[close_idx] == ')':
                        left -= 1
                    close_idx += 1
                cur_num = self.calculate(s[idx + 1:close_idx - 1])
                idx = close_idx
                continue
            else:
                if prev_op == '+':
                    stack.append(cur_num)
                elif prev_op == '-':
                    stack.append(-cur_num)
                elif prev_op == '*':
                    stack.append(stack.pop() * cur_num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / cur_num))
                cur_num = 0
                prev_op = c
            idx += 1
        return sum(stack)
    
    # 优化过后的sol
    # t O(n)  s O(n)
    def calculate2(self, s: str) -> int:
        q = deque()
        for c in s + '+':
            if c == ' ':
                continue
            else:
                q.append(c)
        
        def calculate_helper(q: deque) -> int:
            stack = []
            cur_num = 0
            prev_op = '+'

            while q:
                c = q.popleft()
                if c == '(':
                    cur_num = calculate_helper(q)
                elif c.isdigit():
                    cur_num = cur_num * 10 + int(c)
                elif c == ')': # 和 basci calculator ii 最大的不同就是)结束之后要把之前的operation处理完放进stack里进去
                    if prev_op == '+':
                        stack.append(cur_num)
                    elif prev_op == '-':
                        stack.append(-cur_num)
                    elif prev_op == '*':
                        stack.append(stack.pop() * cur_num)
                    elif prev_op == '/':
                        stack.append(int(stack.pop() / cur_num))
                    break
                else:
                    if prev_op == '+':
                        stack.append(cur_num)
                    elif prev_op == '-':
                        stack.append(-cur_num)
                    elif prev_op == '*':
                        stack.append(stack.pop() * cur_num)
                    elif prev_op == '/':
                        stack.append(int(stack.pop() / cur_num))
                    cur_num = 0
                    prev_op = c
                
            return sum(stack)
        
        return calculate_helper(q)


s = Solution()
print(s.calculate2('5-(3+2)*5+3'))

# 但计算'3-2*2'
# stack里面[3], [3, -2], [3, -4]，每次都是在operator的位置(+-*/)，计算上一个operator的值并放入到stack里面
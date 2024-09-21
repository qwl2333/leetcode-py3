# lc 227
class Solution:
    def calculate(self, s: str) -> int:
        stack, cur_num, prev_op = [], 0, '+' # cur_num是记录连续数字的，起始值为0，默认的previous operator也是+, 为什么呢？
                                              # 如果是‘3-2*2', 那么到'-'时因为cur_num初始为0，可以得到3，其他初始值得不到3, prev_op='+', 会把3加到stack里面去
                                              # 如果是‘-3-2*2’，那么到第一个'-'时，因为cur_num初始为0，last_op='+'，会把0加到stack里面去
        for c in s + '+': # the last added operator could be any of + - * /, it aims to do one more loop and add value to the stack
            if c == ' ': # 这里必须用' ', 不可以用 if not c: 因为' ' is truthy
                continue

            if c.isdigit():
                cur_num = (cur_num * 10) + int(c)
            else:
                if prev_op == '-':
                    stack.append(-cur_num)
                elif prev_op == '+':
                    stack.append(cur_num)
                elif prev_op == '*':
                    stack.append(stack.pop() * cur_num)
                elif prev_op == '/':
                    stack.append(int(stack.pop() / cur_num)) # 这个int()是truncate towards zero, 如果用//，floor division，那么-3//2=-2 而不是-1
                cur_num, prev_op = 0, c
        return sum(stack)

s = Solution()
print(s.calculate('3-2*2'))

# 但计算'3-2*2'
# stack里面[3], [3, -2], [3, -4]，每次都是在operator的位置(+-*/)，计算上一个operator的值并放入到stack里面
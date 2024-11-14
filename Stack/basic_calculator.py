# lc 224
from collections import deque
class Solution:
    '''
    这个解法是基于 772 basic calculator iii 最优解改编的
    1. 最优解没有用到stack, 用 sum, prev_num, cur_num, prev_op
    现在分析下每一个variable的作用以及为什么需要这些
    首先sum好理解是accumulate所有之前的操作的和
    cur_num: 代表最近的一个数
    pre_num: 代笔比cur_num还要前面的一个数,目的是为了做*/的操作
    prev_op: 必须记录之前的operator, 因为每次计算必须发生在operator的位置, 不可能发生在数字的位置, 
    理由是你并不知道数字有没有结束, 所以当计算发生在operator时, 我并不知道当前operator之后的数字是什么
    没法计算, 只能计算之前operator的, 所以必须要记录之前的operator是什么
    好, 分析完772, 再分析224需要怎么多variables的哪几个
    sum, cur_num, prev_op都是必须的理由和上面写的一样
    只有pre_num不需要了, 因为224只有+-操作
    '''
    def calculate(self, s: str) -> int:
        q = deque()
        for c in s + '+': # 为什么加+, 和为什么需要记录pre_op的理由类似, 我们的计算只能发生在operatpr的地方,所以最后要补一个dummy operator
            if c == ' ':
                continue
            else:
                q.append(c)
        
        def calculate_helper(q: deque) -> int:
            sum = 0
            cur_num = 0
            prev_op = '+'

            while q:
                c = q.popleft()
                if c == '(':
                    cur_num = calculate_helper(q)
                elif c.isdigit():
                    cur_num = cur_num * 10 + int(c)
                elif c == ')':
                    if prev_op == '+':
                        sum += cur_num
                    elif prev_op == '-':
                        sum -= cur_num
                    return sum
                else:
                    if prev_op == '+':
                        sum += cur_num
                    elif prev_op == '-':
                        sum -= cur_num
                    cur_num = 0
                    prev_op = c

            return sum
        
        return calculate_helper(q)

a = Solution()
print(a.calculate('1-(     -2)'))
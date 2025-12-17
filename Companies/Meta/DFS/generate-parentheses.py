# lc 22
# Time: O(Cₙ × n) Catalan Number（卡特兰数) Cₙ = C₀Cₙ₋₁ + C₁Cₙ₋₂ + C₂Cₙ₋₃ + ... + Cₙ₋₁C₀
# Space: O(n)（不算输出空间）
class Solution:
    '''
    cur: 当前已经拼好的字符串

    open_left: 还能放多少个 '('

    close_left: 还能放多少个 ')'

    backtracking: 走一条路 → 不行 → 撤销这一步（回到上一个状态）→ 换别的选择
    这种依靠 cur: str的不变性 stack 返回时上一个cur str还在而且值是不变的
    '''
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def dfs(cur: str, open_left: int, close_left: int):
            # 括号都用完了，得到一个合法结果
            if open_left == 0 and close_left == 0:
                res.append(cur)
                return

            # 还能放 '(' 就放
            if open_left > 0:
                dfs(cur + '(', open_left - 1, close_left)

            # 右括号必须比左括号少用一些，才能放 ')'
            if close_left > open_left:
                dfs(cur + ')', open_left, close_left - 1)

        dfs("", n, n)
        return res
    '''
    res 得到的顺序是
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
    '''

    '''
    传统的原地append + pop的backtracking
    '''
    def generateParenthesis_bt(self, n: int) -> list[str]:
        res = []
        path = []

        def backtrack(open_used: int, close_used: int):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if open_used < n:
                path.append('(')
                backtrack(open_used + 1, close_used)
                path.pop()              # <-- 撤销选择

            if close_used < open_used:
                path.append(')')
                backtrack(open_used, close_used + 1)
                path.pop()              # <-- 撤销选择

        backtrack(0, 0)
        return res
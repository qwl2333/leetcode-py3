# lc 10 和 lc 44 类似
# 区别是 lc 10 必须根据 * 之前的char来match, lc 44是 *。可以match任何sequence of chars, even empty sequence
class Solution:
    """
    状态定义 dp(i, j): 
    s 从索引 i 开始的后缀，是否能被模式 p 从索引 j 开始的后缀所匹配。
    
    1. 具体例子的含义变化:
       假设 s = "aab", p = "c*a*b"
       - dp(0, 0): 语义 "aab" 是否匹配 "c*a*b"? 
                  动作: 发现 p[1] 是 '*', 尝试匹配 0 次 'c'。
       - dp(0, 2): 语义 "aab" 是否匹配 "a*b"? (由 dp(0, 0) 跳过 "c*" 而来)
                  动作: 发现 p[3] 是 '*', 且 s[0] == p[2], 尝试匹配 1 次 'a'。
       - dp(1, 2): 语义 "ab" 是否匹配 "a*b"? (由 dp(0, 2) 消耗 s[0] 后递归而来)
    
    2. 递归状态转移的本质:
       - 匹配普通字符 -> dp(i + 1, j + 1):
         语义: 当前字符相等，看剩下的字符串和剩下的模式是否匹配。
       - 处理 x* 匹配 0 次 -> dp(i, j + 2):
         语义: 忽略 x*，跳过模式里的这两个字符，看当前的字符串和跳过后的模式是否匹配。
       - 处理 x* 匹配 1 次或多次 -> dp(i + 1, j):
         语义: 当前匹配了 x, 消耗 s 的一个字符，但模式 p 不动(x* 还能接着用)，看剩下的 s 是否匹配当前的 p。

    3. 具体推演例子 (Trace): s = "ab", p = ".*"
       - dp(0, 0): s="ab", p=".*". 
                  first_match=True ('.'匹配'a'). 发现p[1]=='*', 进入分支:
                  -> 选项A (0次): dp(0, 2) -> j=2 达末尾但 i=0, 返回 False
                  -> 选项B (1次+): first_match为True, 调用 dp(1, 0)
       - dp(1, 0): s="b", p=".*". 
                  first_match=True ('.'匹配'b'). 再次进入'*'分支:
                  -> 选项A (0次): dp(1, 2) -> j=2 达末尾但 i=1, 返回 False
                  -> 选项B (1次+): first_match为True, 调用 dp(2, 0)
       - dp(2, 0): s="", p=".*". 
                  first_match=False (s已空). 进入'*'分支:
                  -> 选项A (0次): dp(2, 2) -> i=2, j=2 触发 Base Case, 返回 True!
                  -> 选项B (1次+): first_match为False, 此路不通
       - 结果回溯: dp(2, 0)返回True -> dp(1, 0)返回True -> dp(0, 0)返回True.

    tc: O(S * P) S和P 分别是字符串s和模式p的长度。逻辑: 因为有了 memo 记忆化，每个状态 (i, j) 只会被计算一次。总共有(S+1)*(P+1)个状态，每个状态内部的操作(判断、查表)都是O(1)的，所以总时间是乘积。
    sc: 逻辑：我们需要一个哈希表或二维数组来存储所有的计算结果，这占用 O(S * P) 的空间。 关于递归深度：递归调用栈的最坏深度是 O(S + P)（当模式不断匹配或跳过时）
    """
    def isMatch(self, s: str, p: str) -> bool:
        # memo 用于存储已经计算过的状态 (i, j)
        memo = {}

        def dp(i, j) -> bool:
            """
            语义: s从索引 i 开始的后缀，是否匹配 p 从索引 j 开始的后缀？
            """
            # 查表，避免重复计算
            if (i, j) in memo:
                return memo[(i, j)]

            # Base Case: 模式用尽，看字符串是否也刚好用尽
            # s = "ab", p = ".*" 这个例子可以看到一步一步如何从dp(0,0)变成dp(0,2) 然后在这里返回的true
            # s = "abc", p = "ab" 这个例子在这里返回false
            if j == len(p):
                return i == len(s)

            # 判断当前字符是否匹配 (s 没到头 且 字符相同或为 '.')
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # 处理 '*' 逻辑
            if j + 1 < len(p) and p[j+1] == '*':
                # 选项 1: 匹配 0 次 x* -> dp(i, j + 2)
                # 选项 2: 匹配 1 次或多次 -> first_match 且 dp(i + 1, j)
                res = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # 普通字符匹配
                res = first_match and dp(i + 1, j + 1)

            # 记录并返回结果
            memo[(i, j)] = res
            return res

        return dp(0, 0)
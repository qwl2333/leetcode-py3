# lc 44 和 lc 10 类似
class Solution:
    """
    这个了解一下, lc 10类似的dp + memo的解法, 会超时, 直接看下面greedy解法
    1. 状态定义 dp(i, j): 
       s 从索引 i 开始的后缀，是否能被模式 p 从索引 j 开始的后缀所匹配。

    2. 递归状态转移的本质 (关键区别在于 '*'):
       - 如果 p[j] 是 '?' 或 p[j] == s[i]:
         语义: 当前字符匹配成功，看剩下的部分: dp(i + 1, j + 1)。
       
       - 如果 p[j] 是 '*':
         语义: '*' 可以匹配空，也可以匹配一个或多个。
         -> 选项A (匹配 0 个): dp(i, j + 1) (跳过这个 '*', 看剩下的模式能不能匹配当前 s)
         -> 选项B (匹配 1 个或多个): dp(i + 1, j) (消耗 s 的一个字符，但模式停在 '*', 等待下次继续匹配)
         只要其中一个成功, dp(i, j) 就为 True。

    3. 具体推演例子 (Trace): s = "adceb", p = "*a*b"
       - dp(0, 0): s="adceb", p="*a*b". p[0]是'*'.
                  -> 选项A (0个): dp(0, 1) -> s="adceb", p="a*b". 匹配! (后续推演略)
                  -> 选项B (1个+): dp(1, 0) -> s="dceb", p="*a*b". 
       在这个过程中，'*' 就像一个“万能胶”，它可以吞掉 'dce' 这段字符。

    4. 复杂度分析:
       - 时间复杂度 (TC): O(S * P)
         其中 S 和 P 分别是字符串 s 和模式 p 的长度。每个状态 (i, j) 只计算一次。
       - 空间复杂度 (SC): O(S * P)
         哈希表存储 S * P 个状态。递归深度最大为 O(S + P)。
    """
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            # 查表
            if (i, j) in memo:
                return memo[(i, j)]

            # Base Case 1: 模式走完
            if j == len(p):
                return i == len(s)

            # Base Case 2: 字符串走完 (但模式还没走完)
            if i == len(s):
                # 只有剩下的模式全是 '*'，才能匹配成功
                return p[j] == '*' and dp(i, j + 1)

            # 核心匹配逻辑
            if p[j] == '*':
                # 匹配 0 个字符 (dp(i, j+1)) OR 匹配 1 个字符并继续 (dp(i+1, j))
                res = dp(i, j + 1) or dp(i + 1, j)
            elif p[j] == '?' or p[j] == s[i]:
                # 当前匹配，向后移动一位
                res = dp(i + 1, j + 1)
            else: # p[j] ！= '*' and (p[j] != '?' and p[j] != s[i)
                # 字符不匹配
                res = False

            memo[(i, j)] = res
            return res

        return dp(0, 0)

    # 上面的解法 O(S*P) 在leetcode中会超时, 要用greedy + 双指针
    #
    # 1. 变量定义:
    #    s_ptr, p_ptr: 当前正在比对的字符串和模式的索引。
    #    last_s_ptr, last_p_ptr: 记录上一次遇到 '*' 时的位置（回溯点/锚点）。
    #    - last_p_ptr: 记录星号在模式中的位置。
    #    - last_s_ptr: 记录星号匹配到字符串的哪个位置。
    #
    # 2. 逻辑本质:
    #    - 贪心策略：遇到 '*' 时，先假设它匹配 0 个字符，继续往后走。
    #    - 回溯机制：如果后面发现走不通了，就回到上一个星号处，让它多吞掉一个字符，再重新尝试。
    #
    # 3. 具体推演例子 (Trace): s = "abc", p = "*?c"
    #    - 初始: s_ptr=0, p_ptr=0, last_s_ptr=-1, last_p_ptr=-1
    #    - 第一步: p[0] 是 '*', 进入 elif p[p_ptr] == '*':
    #             记录锚点: last_p_ptr = 0, last_s_ptr = 0
    #             p_ptr 移向下一位: p_ptr = 1 (指向 '?')
    #    - 第二步: 此时 p[1] 是 '?', 进入 if (match):
    #             '?' 匹配了 s[0] ('a')。
    #             s_ptr = 1, p_ptr = 2 (指向 'c')
    #    - 第三步: 此时 s[1] 是 'b', p[2] 是 'c'。不匹配! 进入 elif last_p_ptr != -1 (触发回溯):
    #             p_ptr 回到星号的后一位: p_ptr = last_p_ptr + 1 = 1 (回到 '?')
    #             让星号多匹配一个: last_s_ptr += 1 = 1
    #             s_ptr 从新的位置开始: s_ptr = 1 (现在 '?' 匹配 s[1] 即 'b')
    #    - 第四步: 此时 p[1] 是 '?', 匹配 s[1] ('b')。
    #             s_ptr = 2, p_ptr = 2 (指向 'c')
    #    - 第五步: s[2] 是 'c', p[2] 是 'c'。匹配!
    #             s_ptr = 3, p_ptr = 3
    #    - 结束: s_ptr 到头，p_ptr 也到头。返回 True。
    #
    # 4. 复杂度分析:
    #    - 时间复杂度 (TC): 平均 O(S + P)，最坏 O(S * P)。
    #               最坏情况 (Worst Case Example):
    #                   - 例子: s = "aaaaaaaaab", p = "*aaaaa"
    #                   - 原因: 模式星号后有一长段与字符串极度相似的字符。
    #                   - 表现: 每次比对到模式末尾发现不匹配时，指针都要回溯到星号处。
    #                   - 结果: 字符串每个位置都会触发一次 O(P) 的扫描，导致时间复杂度退化。
    #      在大多数实际场景下，指针不需要频繁回溯，速度极快。
    #    - 空间复杂度 (SC): O(1)。
    #      只使用了四个整型指针，没有递归栈或额外的数组空间。
    def isMatchGreedy(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        last_s_ptr = -1
        last_p_ptr = -1
        
        while s_ptr < len(s):
            # --- 顺序逻辑解析 ---
            
            # 第一优先级：精确匹配 (字符相等 或 '?')
            # 为什么放在最前面？因为我们总是倾向于“先按部就班走位”。
            # 如果当前能对上，我们就假设这是正确的路径，先走走看。
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1
            
            # 第二优先级：遇到新星号 '*'
            # 如果不能精确匹配，但看到了星号，这就是我们的“保命符”。
            # 我们记下这个位置，先贪心地假设它匹配空串（p_ptr + 1）。
            elif p_ptr < len(p) and p[p_ptr] == '*':
                last_p_ptr = p_ptr
                last_s_ptr = s_ptr
                p_ptr += 1
            
            # 第三优先级：回溯
            # 既不能匹配，也没看到新星号，但如果以前见过星号，
            # 说明我们之前的“贪心”太乐观了。回到旧星号处，多吃一个字符，重来。
            elif last_p_ptr != -1:
                p_ptr = last_p_ptr + 1
                last_s_ptr += 1
                s_ptr = last_s_ptr
            
            # 第四优先级：死路一条
            # 既没法匹配，也没星号救命。
            else:
                return False
        
        # 结尾处理：如果字符串走完了，模式后面还有星号，它们都可以匹配空串。
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)
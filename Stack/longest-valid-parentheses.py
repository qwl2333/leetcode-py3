# lc 32
class Solution:
    # t O(n) s O(1)
    def longestValidParenthesesBest(self, s: str) -> int:
        max_len = 0
        
        # 本质上是从左往右,一旦先出现右括号)，就是无可挽回的情况,后面出现的左括号(不可能配平这个之前出现的)， 比如)(
        # 同样从右往左，一旦先出现左扩好(，后面出现的右括号) 不可能配平之前出现的(

        # 1. 从左向右扫描 (处理右括号过多的情况) eg: ()())()()() (右边多了) 可以算出最长,但是左边多了的情况算的不准确 比如()()(()()()
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                # 左右数量相等，形成有效闭环，更新长度
                max_len = max(max_len, 2 * right)
            elif right > left:
                # 右括号多了，前面断掉了，计数器归零
                left = right = 0
        
        # 2. 从右向左扫描 (处理左括号过多的情况) eg: ()()(()()() (左边多了)
        left = right = 0
        for c in reversed(s): # range(n - 1, -1, -1)
            if c == '(':
                left += 1
            else:
                right += 1
            
            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                # 左括号多了，归零
                left = right = 0
                
        return max_len
 
    def longestValidParentheses(self, s: str) -> int:
        # 利用stack记录idx，)的时候pop，然后计算substring的长度
        # Stack 里的元素（包括那个 -1），本质上是“上一段无法被匹配的那个坏字符的下标”，注意这个坏字符可以是(,也可以是)
        stack = list([-1]) # 一开始给一个假idx-1方便计算, stack存的是一个idx，[idx + 1, i]可以组成一个valid parentheses
        max_len = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack: # 如果遇到))()，这种情况，-1被pop出来之后，要加入一个新的start index 作为新的无法被匹配的坏字符
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len

    # t O(n) s O(n)
    def longestValidParenthesesDP(self, s: str) -> int:
        n = len(s)
        if n < 2:
            return 0

        dp = [0 for _ in range(n)]
        if s[0] == '(' and s[1] == ')':
            dp[1] = 2
        else:
            dp[1] = 0

        for i in range(2, n):
            if s[i] == ')':
                if s[i - 1] == '(':
                    dp[i] = dp[i - 2] + 2
                else: # s[i - 1] == ')':     ( ( . . ） ）
                      #                      0 1 2 3 4 5   对于i=5 的 ) 来说, j=0处 如果是( 就可以形成一个match
                      # j = i - 1 - dp[i - 1]
                    j = i - 1 - dp[i - 1]
                    if j >= 0 and s[j] == '(':
                        # 如果 s[j] == '('，说明配对成功！长度由三部分组成
                        # 1. 2：当前的 ) 和 j 位置的 (
                        # 2. dp[i-1]：中间包裹的长度 
                        # 3. dp[j-1]：j 前面可能还有一段有效子串（把两段连起来）。
                        # dp[i] = dp[i-1] + 2 + dp[j - 1]
                        dp[i] = dp[i - 1] + 2 + (dp[j - 1] if j - 1 >= 0 else 0)
        
        return max(dp)

s = Solution()
print(s.longestValidParentheses('))()(())')) # )()()()(
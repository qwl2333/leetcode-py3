# lc 1209 和 lc 1047类似
class Solution:
    # 时间复杂度 O(N)：无论 k 是多少，我们依然只遍历一遍字符串，每个元素的操作都是 O(1)
    # 空间复杂度 O(N)：栈的大小在最坏情况下与字符串长度成线性关系
    # 如果用lc 1047的方法每次弹出一个而且不记录个数, 那可能就是 O(N * k) 的复杂度
    def removeDuplicates(self, s: str, k: int) -> str:
        # stack 存储格式：[字符, 连续出现的次数]
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                # 1. 遇到相同的，直接增加计数器
                stack[-1][-1] += 1
                # 2. 如果达到 k，瞬间爆炸（弹出）
                if stack[-1][-1] == k:
                    stack.pop()
            else:
                # 3. 遇到不同的，开启新的计数
                stack.append([c, 1])
        
        # 4. 重组字符串：将字符重复对应的次数
        res = ''
        while stack:
            c, freq = stack.pop()
            res += (c * freq)
        
        return res[::-1]
                
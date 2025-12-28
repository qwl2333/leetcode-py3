# lc 394
class Solution:
    # TC: O(L) L 是解码后生成的字符串的总长度。我们需要遍历输入字符串，并且最终构建出解码后的结果
    # SC: O(M + L). M 是括号的最大嵌套深度（栈的空间），L 是存储最终结果所需的空间。
    '''
    M dominant
    1[a1[b1[c1[d]]]]最终字符串长度L只有 4 ("abcd")。但栈的深度M 是 4(有四层嵌套)。此时, M 对空间复杂度的贡献就变得明显了。

    L dominant
    100[a]输入字符串长度很短。栈的深度 M 只有 1(只有一层括号)。但最终字符串长度L 是 100。此时, O(M+L) 中占主导地位的是L。
    '''
    
    def decodeString(self, s: str) -> str:
        stack = []  # 存放 (之前的字符串, 当前数字)
        curr_num = 0
        curr_str = ""
        
        for char in s:
            if char.isdigit():
                # 处理多位数，如 "100"
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # 遇到左括号，将当前进度的字符串和数字压栈
                stack.append((curr_str, curr_num))
                # 重置，开始处理括号内部
                curr_str = ""
                curr_num = 0
            elif char == ']':
                # 遇到右括号，出栈
                prev_str, num = stack.pop()
                # 核心逻辑：上一个字符串 + (当前的重复次数 * 当前括号内的字符串)
                curr_str = prev_str + num * curr_str
            else:
                # 普通字母，直接累加
                curr_str += char
                
        return curr_str
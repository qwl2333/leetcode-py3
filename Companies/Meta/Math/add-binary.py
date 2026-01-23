# lc 67 和 lc 2 类似
from collections import deque
class Solution:
    # TC: O(max(len(a), len(b))) SC: O(max(len(a), len(b)))
    def addBinary(self, a: str, b: str) -> str:
        res = deque()
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        # 只要还有数没加完，或者还有进位，就继续循环
        while i >= 0 or j >= 0 or carry != 0:
            # 1. 拿到当前位的值，如果指针已经到头了就补 0
            val_a = int(a[i]) if i >= 0 else 0
            val_b = int(b[j]) if j >= 0 else 0

            # 2. 计算当前总和
            total = val_a + val_b + carry

            # 3. 更新进位和当前位结果
            carry = total // 2
            new_val = total % 2
            res.appendleft(str(new_val))

            # 4. 指针左移
            i -= 1
            j -= 1
        
        # list to str
        return ''.join(res)

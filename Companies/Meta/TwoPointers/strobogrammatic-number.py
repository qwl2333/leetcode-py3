# lc 246
class Solution:
    # T O(n) S O(1)
    def isStrobogrammatic(self, num: str) -> bool:
        # 定义中心对称的映射关系
        # 数字,旋转后结果,约束
        #   0,       0,必须是自身
        #   1,       1,必须是自身
        #   8,       8,必须是自身
        #   6,       9,必须是对方
        #   9,       6,必须是对方
        strobogrammatic_map = {
            '0': '0',
            '1': '1', 
            '8': '8',
            '6': '9',
            '9': '6'
        }

        l, r = 0, len(num) - 1

        while l <= r:
            l_char = num[l]
            r_char = num[r]

            if l_char not in strobogrammatic_map or r_char not in strobogrammatic_map:
                return False
            # For the number to be strobogrammatic, the rotated leftmost digit must match the rightmost digit.
            if strobogrammatic_map[l_char] != r_char or strobogrammatic_map[r_char] != l_char:
                return False
            
            l += 1
            r -= 1
        
        return True

        
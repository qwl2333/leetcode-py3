# lc 9
class Solution:
    # 时间复杂度 (TC): O(log_10 N) 我们每次循环都将数字除以10, 所以循环次数取决于数字的位数。
    # 空间复杂度 (SC): O(1) 我们只使用了常数个变量来存储反转的结果
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = x
        reverted_num = 0
        while x != 0:
            reverted_num = 10 * reverted_num + x % 10
            x = x // 10
        
        return True if reverted_num == num else False

    # 和上面解法一个意思,但是只用反转一半的数字, tc sc 一样不变
    def isPalindromeHalf(self, x: int) -> bool:
        # 特殊情况处理：
        # 1. 负数不是回文
        # 2. 如果数字最后一位是0，为了是回文，第一位也必须是0，只有0本身满足, 如果不在这里判断是不是0结尾, 当x=10时, 会导致返回true, 因为35行会认为x=010
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_num = 0
        # 当 x > reverted_num 时，说明还没处理到一半
        while x > reverted_num:
            # 拿到最后一位并加到反转结果中
            reverted_num = reverted_num * 10 + x % 10
            # 原始数字去掉最后一位
            x //= 10

        # 当数字长度为偶数时，x == reverted_num
        # 当数字长度为奇数时，我们可以通过 reverted_num // 10 去掉中间那位（不影响回文判断）
        # 例如：12321 -> 处理完后 x = 12, reverted_num = 123
        return x == reverted_num or x == reverted_num // 10

s = Solution()
print(s.isPalindromeHalf(10))
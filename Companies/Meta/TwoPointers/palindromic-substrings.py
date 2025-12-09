# lc 647
class Solution:
    # tc O(n^2) sc O(1)
    # 中心扩展法
    # abcc 一共有 a, b, c, c, ab, bc, cc   2 * n -1 种可能的中心点 n 是 s的长度
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        count = 0
        for c in range(2 * N - 1): # 0 - 6
            # 这个c没啥特别含义, 主要是来判断中心点的l r可能指向同一个点,也可能正好是两个相邻的点
            l = N // 2
            r = l + c % 2

            while l >= 0 and r < N and s[l] == s[r]:
                count += 1
                l += 1
                r -= 1
        return count

        
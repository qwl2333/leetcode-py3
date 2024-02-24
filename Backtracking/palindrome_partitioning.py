# lc 131
class Solution:
    # time -  O(n * 2^n), O(2^n) is number of strings, each string takes O(n) time to generate new string and check
    # if it is a palindrome, why 2^n, imagining 'aaa',
    # aaa
    # a    aa    aaa
    # a aa   a
    # a
    # it would be 2^3 at most since all substrings are palindrome
    # space O(n) - n is length of str, used for stack memory
    def partition(self, s: str) -> list[list[str]]:
        res = []
        part = []

        def dfs(i: int): # 从s[i]开始找回文串，找到一个，就进入下一层，同时更新i位置
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)): 
                if self.is_palin(s, i, j): # 从i开始，找到一个回文串，就进入下一城
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return res
    
    def is_palin(self, s: str, start: int, end: int):
        while start < end:
            if s[start] != s[end]:
                return False

            start += 1
            end -= 1
        return True

s = Solution()
print(s.partition('aab'))
# lc 139
class Solution:
    '''
    dp解法
    dp[i]表示 s[:i]是可以被break的
    如果此时s[:i]可以被break
    那么一定是i的左边存在一个位置start, dp[start]=true 并且 s[start:i] 存在于 wordDict里面
    Time complexity: O(n * m * k)
    n is length of input string s.
    m is number of words in wordDict
    k is average size of substrings.

    Space complexity: O(n)
    '''
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [False for _ in range(n + 1)] # dp[i]意思是 s[:i] 是可以被break的, i表示的是substring的长度
        dp[0] = True
        for i in range(1, n + 1): # # i表示的是substring s[:i]的长度, 我们从1开始直到n, 依次算这个s[:i]可不可以被break, 当i=n s[:i]就是原来的s
            for w in wordDict:
                start = i - len(w)
                if start >= 0 and dp[start] and s[start:i] == w:
                    dp[i] = True
                    break

        return dp[n]
    
    '''
     这是我觉得最好记的解法,但是tle了
     Time complexity: O(n * m * k)
     Space complexity: O(n)
     是 dp解法的 wordBreak 的dfs版本
     想象成从左边开始, 不断recursively用 worddict里的word来构建一个target s
    '''
    def wordBreak4(self, s: str, wordDict: list[str]) -> bool:
        memo = {}
        def construct_targe_s(start: int) -> bool:
            if start == len(s): # 构建完成了一个s, 是由worddict里面的word构建完成的
                return True
            
            for word in wordDict:
                end = start + len(word) # end of constructed left substring, note that end - 1 is the index
                if end <= len(s) and s[start:end] == word and construct_targe_s(end):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False

        return construct_targe_s(0)

    # dp解法 O(n^2 * n) n - length of s
    def wordBreak2(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False for _ in range(n + 1)] # dp[i]意思是 s[:i] 是可以被break的, i表示的是substring的长度
        dp[0] = True
        for i in range(1, n + 1): # i表示的是substring s[:i]的长度, 我们从1开始直到n, 依次算这个s[:i]可不可以被break, 当i=n+1 s[:i]就是原来的s
            for j in range(i):
                print(f'dp[j]: {dp[j]}')
                print(f's[j:i]: {s[j:i]}')
                if dp[j] and s[j:i] in word_set: # s[j:i] in the worst case took O(i)
                    dp[i] = True
                    break
        
        return dp[n]
    
    # dfs + memo O(n^2 * n) n - length of s 是 dp解法 wordBreak2 的dfs 版本
    def wordBreak3(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)
        memo = {}

        def canBreak(s: str):
            if not s:
                return True
            if s in memo:
                return memo[s]
            
            for i in range(1, len(s) + 1): # i stands for the length of left substring
                left_sub = s[:i]
                right_sub = s[i:]
                if left_sub in word_set and canBreak(right_sub):
                    memo[s] = True
                    return True
            
            memo[s] = False
            return False
        
        return canBreak(s)


    # 也可以用trie来做

s = Solution()
print(s.wordBreak('leetcode', ["leet","code"]))
class Solution:
    '''
    Time complexity: O(2^n)
    Space complexity: O(n) - depth of the recursion tree
    '''
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        res = []
        def wordBreakHelper(s: str):
            if not s:
                res.append(' '.join(path))
                return
            
            for i in range(1, len(s) + 1):
                left_sub = s[:i]
                right_sub = s[i:]
                if left_sub in word_set:
                    path.append(left_sub)
                    wordBreakHelper(right_sub)
                    path.pop()
        
        path = []
        wordBreakHelper(s)
        return res
    
    '''
    dfs + memo time O(2^n)
    time O(2^n) 
    space O(n) if only consider the depth of recursion tree
    为啥要用memo, 思考例子 s = “abcedf”  word_Dict = {"a", "b", "ab", "ce", "df", "cedf"}
    a, b, ce, df 和 a, b, cedf
    ab, ce, df  和 ab, cedf
    如果不cache memo[cedf] = ['ce df', 'cedf'], s = cedf 就要走两次
    '''
    def wordBreak2(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        res = []
        memo = {}  # A dictionary to store the results of subproblems
        
        def wordBreakHelper(s: str) -> list[str]:
            if s in memo:  # Check if the result for this substring is already computed
                return memo[s]
            
            if not s:
                return ['']
            
            current_result = []
            
            for i in range(1, len(s) + 1):
                left_sub = s[:i]
                right_sub = s[i:]
                
                if left_sub in word_set:
                    rest_of_sentences = wordBreakHelper(right_sub)
                    for sentence in rest_of_sentences:
                        if sentence:
                            current_result.append(left_sub + ' ' + sentence)
                        else:
                            current_result.append(left_sub)
                            
            memo[s] = current_result  # Memoize the result for the current substring
            return current_result
        
        res = wordBreakHelper(s)
        return res
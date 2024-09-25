# lc 17
from collections import deque
class Solution:
    # backtracking Time O(n * 4^n), n - len of digits, 4 is the max number of letters mapped to a digit
    # Space O(n) the recursion call stack could be as long as n
    def letterCombinationsBackTracking(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = []

        def letterCombinationsHelper(idx: int, path: list[str]) -> list[str]:
            if idx == len(digits):
                path_str = ''.join(path) # This join is O(n), that'ss why TC is O(n * 4^n)
                combinations.append(path_str)
                return
            
            letters = phone[digits[idx]]

            for letter in letters:
                path.append(letter)
                letterCombinationsHelper(idx + 1, path)
                path.pop()
        
        letterCombinationsHelper(0, [])
        return combinations
    

    # recursion  Time O(n * 4^n), n - len of digits, 4 is the max number of letters mapped to a digit
    # Space O(n) the recursion call stack could be as long as n
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def letterCombinationsHelper(digits: str) -> list[str]:
            if digits == '':
                return ['']

            letters = phone[digits[0]]

            next_combi = letterCombinationsHelper(digits[1:])

            res = []
            for e in next_combi:
                for letter in letters:
                    res.append(letter + e)

            return res

        return letterCombinationsHelper(digits)

    # 这个是最优解, backtracking 可以不看
    # bfs sol O(number of combinations) O(4^n) 每个digit最多四种选择, 想像成树就是树有四个孩子, 那么树有多高呢, 就是digits的长度n, 所以一共有O(4^n)个节点
    def letterCombinationsBFS(self, digits: str) -> list[str]:
        if not digits:
            return []
        phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        queue = deque([('', -1)])
        res = []

        while queue:
            cur_str, cur_index = queue.popleft()
            next_idx = cur_index + 1
            letters = phone[digits[next_idx]]
            for letter in letters:
                new_str = cur_str + letter
                if len(new_str) == len(digits):
                    res.append(new_str)
                else:
                    queue.append((new_str, next_idx))

        return res

s = Solution()
print(s.letterCombinationsBFS('23'))

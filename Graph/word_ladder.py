# lc 127
from collections import deque
import string
class Solution:
    # BFS time O(n*m^2) n - len(wordList), m - len(word), 为何是m^2, 因为每个word，都有经过26次更换字母，26m，但是拼接新的word，还需要m，所以是26m^2
    # space O(n*m),worst case queue最多可以包含所有letters or maybe half of the letters??，所需空间是len(wordList) * len(word)
    def ladderLengthBFS(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # 1. 预处理: 使用set提高查询效率
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        # 2. 初始化: 队列中存储(当前单词, 当前步数) 因为这个步数的存在我不需要像126那样, 在while循环中先存number_of_nodes_at_current_level
        # 起点单词算第一步
        queue = deque()
        queue.append((beginWord, 1))

        # 3. visit control: 如果起点在word_set中，先移除防止往回走
        if beginWord in word_set:
            word_set.remove(beginWord)
        
        while queue:
            cur_word, step = queue.popleft()

            # 4. 尝试对当前单词的每一个位置进行26个字母的替换
            size = len(cur_word)
            for i in range(size):
                for char in string.ascii_lowercase:
                    # 跳过变成原来cur_word的情况,其实不加这个也可以, 因为cur_word被visit过了不在word_set里面
                    if char == cur_word[i]:
                        continue

                    new_word = cur_word[0:i] + char + cur_word[i+1:]
                    
                    # 5. 检查是否到终点了
                    if new_word == endWord:
                        return step + 1
                    
                    # 6. 如果在集合中, 则加入队列并从集合中移除(防止重复访问)
                    if new_word in word_set:
                        queue.append((new_word, step + 1))
                        word_set.remove(new_word)
        
        return 0

    # DFS TLE time (26^n) n - len of word
    def ladderLengthDFS(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        alphabet = [chr(i) for i in range(ord('a'), ord('z')+1)]
        word_set = set(wordList)
        visited = set()
        self.res = []

        def dfs(begin_word: str, end_word: str, path: list[str]):
            if begin_word == end_word:
                path.append(end_word)
                if self.res == [] or len(self.res) > len(path):
                    self.res = list(path)
                path.pop()
                return
            
            if begin_word in visited:
                return
            
            visited.add(begin_word)
            path.append(begin_word)
            for i in range(len(begin_word)):
                for letter in alphabet:
                    new_word = begin_word[0:i] + letter + begin_word[i + 1:]
                    if new_word not in visited and new_word in word_set:
                        dfs(new_word, end_word, path)
            visited.remove(begin_word)
            path.pop()
            
        path = []
        dfs(beginWord, endWord, path)
        return len(self.res)
# lc 127
from collections import deque
import string
class Solution:
    # BFS time O(n*m^2) n - len(wordList), m - len(word), 为何是m^2, 因为每个word，都有经过26次更换字母，26m，但是拼接新的word，还需要m，所以是26m^2
    # space O(n*m),worst case queue最多可以包含所有letters or maybe half of the letters??，所需空间是len(wordList) * len(word)
    def ladderLengthBFS(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        alphabet = string.ascii_lowercase
        word_set = set(wordList)

        def bfs(begin_word: str, end_word: str) -> int:
            queue = deque([begin_word]) # 也可以选择把level order加到queue里面去
            count = 1
            if end_word not in word_set:
                return 0
            if begin_word in word_set:
                word_set.remove(begin_word)
            while queue:
                number_of_nodes_at_current_level = len(queue)
                for _ in range(number_of_nodes_at_current_level):
                    cur_word = queue.popleft()
                    for i in range(len(cur_word)):
                        for letter in alphabet:
                            new_word = cur_word[0:i] + letter + cur_word[i+1:]
                            if new_word == end_word:
                                return count + 1
                            if new_word in word_set:
                                queue.append(new_word)
                                word_set.remove(new_word)
                count += 1
            return 0
        
        return bfs(beginWord, endWord)

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
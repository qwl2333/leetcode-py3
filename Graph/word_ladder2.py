from collections import deque, defaultdict
import string
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        alphabet = string.ascii_lowercase
        word_set = set(wordList)
        visited = {} # key visited_word, value - 从begin_word出发到visited word最短距离，也就是level order traversal的level
        adjacent_list = defaultdict(list)

        def bfs(begin_word: str, end_word: str) -> int: # bfs find the target and populate a adjacent list
            queue = deque([begin_word])
            if end_word not in word_set:
                return

            visited[begin_word] = 0 # 0 is the level number

            while queue:
                number_of_nodes_at_current_level = len(queue) # number of nodes at current level
                for _ in range(number_of_nodes_at_current_level):
                    cur_word = queue.popleft()
                    for i in range(len(cur_word)):
                        for letter in alphabet:
                            new_word = cur_word[0:i] + letter + cur_word[i+1:]
                            print(new_word)
                            if new_word in word_set and new_word != cur_word:
                                adjacent_list[cur_word].append(new_word)
                                if new_word not in visited:
                                    queue.append(new_word)
                                    visited[new_word] = visited[cur_word] + 1

        bfs(beginWord, endWord)
        # print(visited)
        # print(adjacent_list)
        def dfs(begin_word: str, end_word: str, path: list[str]):
            if begin_word == end_word:
                path.append(begin_word)
                res.append(list(path))
                path.pop()
                return

            path.append(begin_word)
            for nb in adjacent_list[begin_word]:
                if visited[nb] == visited[begin_word] + 1:
                    dfs(nb, end_word, path)
            path.pop()

        res = []
        dfs(beginWord, endWord, [])
        return res            


s = Solution()
print(s.findLadders('hit', 'cog', ["hot","dot","dog","lot","log","cog"]))
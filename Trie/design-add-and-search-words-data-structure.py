# lc 211
class TrieNode:
    def __init__(self):
        self.children = {} # key - letter, value - TrieNode
        self.end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        
        cur.end_of_word = True
        
    def search(self, word: str) -> bool:
        def dfs(idx: int, root: TrieNode) -> bool: # 意思是从word[idx]开始，用root作为TrieNode起点，能不能在字典树里面找到word[idx:]
            cur = root
            for i in range(idx, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else: # word is letter
                    if c not in cur.children:
                        return False
                    else:
                        cur = cur.children[c]
            return cur.end_of_word
        return dfs(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
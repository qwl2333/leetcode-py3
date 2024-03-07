# lc 208
# 插入一个字符串，找是不是存在，这种用hashmap就行，但是字典树不同之处是可以优化startwith
# startwith查找length 为l的前缀prefix，只需要O(l), 如果是hashmap就要遍历所有的key看是不是有这个前缀，在hashmap里面有很多值时非常慢
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.end_of_word        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True         


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
param_2 = obj.search('apple')
param_3 = obj.startsWith('app')
print(param_3)
# similar to lc 208 implement trie
'''
 Remove prefix strings in a list of string {"a", "ab", "abc"} -> {"abc"}
'''
class TrieNode:
    def __init__(self):
        self.children = {} # key: letter, value - TrieNode
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end_of_word = True
    
    def startswith(self, prefix: str) -> bool: # if insert 'abc', startswith('ab') is true but startswith('abc') is false
        cur = self.root
        
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return cur.children != {}

class Solution:
    # Time: O(n * m) n - number of words, m - avg length of word 
    # Space: O(n * m) 
    # 以上是近似的估算
    # 这个范围应该是如果输入是[a,ab,abc,abcd,...],那时间空间就是最长的那个word，
    # 如果输入是[ac,df,cs,ft,..], 那时间空间就是一共有多少个character
    def remove_prefix_from_array(self, input_words: list[str]) -> list[str]:
        trie = Trie()
        res = []
        for word in input_words:
            trie.insert(word)
        
        for word in input_words:
            if not trie.startswith(word):
                res.append(word)
        
        return res

s = Solution()
print(s.remove_prefix_from_array(['a', 'ab', 'd', 'a', 'abc']))

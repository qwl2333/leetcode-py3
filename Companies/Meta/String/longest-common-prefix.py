# lc 14
class TrieNode:
    def __init__(self):
        self.children = {} # char -> TrieNode
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

class Solution:
    # sol1 用 trie
    # time: O(m * n) m - number of str in strs, n - avg len of each string
    # space: O(m * n) 建trie所需空间
    def longestCommonPrefix(self, strs: list[str]) -> str:
        trie = Trie()
        for s in strs:
            if s:
                trie.insert(s)
            else:
                return ''
        cur = trie.root
        count = 0
        while len(cur.children) == 1 and not cur.end_of_word:
            keys = list(cur.children.keys())
            cur = cur.children[keys[0]]
            count += 1
        return strs[0][0:count]
    
    # time O(nmlognm + m) = O(nm * lognm) n - number of str in strs, m - avg length of str, 就是sort严格意义上是sort所有characters
    # space O(1)
    def longestCommonPrefixSortStrs(self, strs: list[str]) -> str:
        strs.sort()
        first = strs[0]
        last = strs[len(strs) - 1]
        count = 0
        for i in range(min(len(first), len(last))):
            c_f = first[i]
            c_l = last[i]
            if c_f == c_l:
                count += 1
            else:
                break
        
        return first[0:count]
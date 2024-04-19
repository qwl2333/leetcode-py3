# lc 72
class Solution:
    # time O(m*n) space 如果不考虑创造出来的新的string的话 O(m*n) n - len(word1), m - len(word2)
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def minDistanceHelper(word1: str, word2: str, idx: int) -> int:
            if word1 == word2:
                return 0
            
            if idx == len(word1) or idx == len(word2):
                return abs(len(word1) - len(word2))
            
            if (word1, word2, idx) in memo:
                return memo[(word1, word2, idx)]
            
            if word1[idx] == word2[idx]:
                return minDistanceHelper(word1, word2, idx + 1)
            else:
                # del
                new_word1_de = word1[0:idx] + word1[idx+1:]
                del_dist = minDistanceHelper(new_word1_de, word2, idx)

                # insert
                new_word1_insert = word1[0:idx] + word2[idx] + word1[idx:]
                insert_dist = minDistanceHelper(new_word1_insert, word2, idx + 1)

                # subs
                new_word1_subs = word1[0:idx] + word2[idx] + word1[idx+1:]
                subs_dist = minDistanceHelper(new_word1_subs, word2, idx + 1)

                res = min(del_dist, insert_dist, subs_dist) + 1
                memo[(word1, word2, idx)] = res
                return res
            
        return minDistanceHelper(word1, word2, 0)
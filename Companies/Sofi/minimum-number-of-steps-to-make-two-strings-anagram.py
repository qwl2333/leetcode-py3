'''
https://www.1point3acres.com/bbs/thread-962307-1-1.html
For each pair of words, how many characters do you have to change in order to make them anagrams? 
Return an array with the number of changes required for each pair. 
Return -1 if the pair cannot be made into anagrams.
'''
# lc 1347
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = [0] * 26
        count_t = [0] * 26

        for char in s:
            count_s[ord(char) - ord('a')] += 1

        for char in t:
            count_t[ord(char) - ord('a')] += 1

        steps = 0
        for i in range(26):
            steps += abs(count_s[i] - count_t[i])

        return steps // 2   
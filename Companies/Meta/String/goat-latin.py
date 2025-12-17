# lc 824
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = 'aeiouAEIOU'
        word_list = sentence.split(' ')
        res = []
        for i, word in enumerate(word_list):
            if word[0] in vowels:
                word += 'ma'
            else:
                word = word[1:] + word[0] + 'ma'
            word += (i + 1) * 'a'
            res.append(word)
        return ' '.join(res)

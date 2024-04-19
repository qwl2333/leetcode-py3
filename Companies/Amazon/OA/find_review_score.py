# review = 'GoodProductButScrapAfterWash'
# prohibitedWords = ['crap', 'odpro']
# 双指针 右指针走直到包含一个prohibited word，左指针走知道不包含任何prohibited word
class Solution:
    def find_review_score(self, review: str, prohibited_words: list[str]) -> int:
        review = review.lower()
        l, r = 0, 0
        n = len(review)

        def not_include_prohibited_words(substr: str) -> bool:
            for w in prohibited_words:
                if w in substr:
                    return False
            
            return True
        
        score = 0
        while r < n:
            substr = review[l : r + 1]
            if not_include_prohibited_words(substr):
                score = max(score, r - l + 1)
                r += 1
            else:
                while not not_include_prohibited_words(review[l : r + 1]):
                    l += 1
        
        return score

s = Solution()
print(s.find_review_score('GoodProductButScrapAfterWash', ['odpro', 'crap']))


        




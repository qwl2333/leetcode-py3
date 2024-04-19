class Solution:
    def get_longest_match(self, text: str, regex: str) -> int:
        prefix, suffix = regex.split('*')
        len_p = len(prefix)
        len_s = len(suffix)
        if len_p == 0 and len_s == 0:
            return len(text)
        
        p_s = text.find(prefix)
        p_e = p_s + len_p - 1
        s_s = text.rfind(suffix)
        s_e = s_s + len_s - 1
        if len_p > 0 and len_s > 0:
            if p_e >= s_s:
                return -1
            return s_e - p_s + 1

        if len_p == 0:
            # len_s 必定不为0，因为开头已经排除了同时为0的情况
            return s_e + 1
        if len_s == 0:
            return len(text) - p_s

    # Two pointers find first occurance of target om text_string, time O(n)
    def find_first_occurance(self, text_string: str, target: str) -> list[int]:
        result = []
        l, r = 0, 0
        t = 0
        while r < len(text_string):
            while r < len(text_string) and text_string[r] != target[t]:
                r += 1
                l = r
            while r < len(text_string) and t < len(target) and text_string[r] == target[t]:
                r += 1
                t += 1
            if t == len(target):
                result = [l, r - 1]
                return result
            t = 0

        return result
    
s = Solution()
print(s.get_longest_match('hackerrank', 'ack*r'))
# lc 443
class Solution:
    # Time O(n), Space O(1)
    def compress(self, chars: list[str]) -> int:
        l, r, z = 0, 0, 0
        n = len(chars)
        while r < n:
            while r < n and chars[l] == chars[r]:
                r += 1
            if r == n:
                break
            length = r - l
            if length > 1:
                chars[z] = chars[l]
                z += 1
                s_len = str(length)
                for num in s_len:
                    chars[z] = num
                    z += 1
            else:
                chars[z] = chars[l]
                z += 1
            l = r
        
        length = r - l
        if length > 1:
            chars[z] = chars[l]
            z += 1
            s_len = str(length)
            for num in s_len:
                chars[z] = num
                z += 1
        else:
            chars[z] = chars[l]
            z += 1
        print(chars)
        return z

s = Solution()
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))
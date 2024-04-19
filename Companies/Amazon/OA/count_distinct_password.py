from collections import defaultdict
class Solution:
    # 此题是给一个password，每次reverse一个substring都可以变成别的password，问有多少个不同的password
    # 比如abc，只reverse长度为一的substring，那就还是abc
    # reverse长度为2的substring，abc -> bac, acb
    # reverse长度为3的substring，abc -> cba

    # Brute force 解法 O(n^3) 两遍n循环，里面字符串拼接还需O(n)的操作
    def count_distinct_password(self, password: str) -> int:
        n = len(password)
        word_set = set([password])
        for i in range(n):
            for j in range(i+1, n+1):
                sub_str = password[i:j]
                new_password = password[:i] + sub_str[::-1] + password[j:]
                print(sub_str)
                print(f'new password: {new_password}')
                word_set.add(new_password)
        return len(word_set)
    
    # dp[][] 二维数组  dp[i][j] 表示password[i]与password[j]不同为1，相同为0
    # 对于任意一个password[i]，只需要计算之前（或者之后）有几个和当前char不同的char出现的次数，累加起来就是有效的字符串的个数
    # 因为b...a, 只要首位不同，reverse之后必不同，这个代表的数从idx_b到idx_a的不同与原始密码的一个新字符串
    # 中间是什么样不用管，因为现在计算的是从idx_b到idx_a字符串，而且中间的计算应该是(idx_b+1,idx_a-1)，这之间如果有新的字符串也会被
    # 统计进去，新字符串就是reverse（idx_i，idx_j）之后不同于原始密码的字符串
    # time - O(n^2) spac - O(1) 如果不用dp[][]
    def count_distinct_password_dp(self, password: str) -> int:
        n = len(password)
        dp = [[0 for c in range(n)] for r in range(n)] # dp[i][j]表示password[i]与password[j]不同为1，相同为0
        # 其实不需要dp，直接算count也行
        count = 0
        for i in range(n):
            for j in range(i, n):
                print(f'i:{i}, j{j}')
                if password[i] != password[j]:
                    dp[i][j] = 1
                    count += 1
        return count
    
    # 依然是dp思想，找当前i之前[0,i-1]的不同于password[i]的字母的个数
    # time - O(n), space - O(1)
    def count_distinct_password_dp2(self, password: str) -> int:
        n = len(password)
        visited = defaultdict(int) # 统计已经走过的字母的出现的频率
        count = 0
        for i in range(n):
            cur_c = password[i]
            visited[cur_c] = visited[cur_c] + 1
            diff = i + 1 - visited[cur_c] # 当前长度减去已经visited过的重复的password[i]，就是前面所有不同于password[i]的字母的个数
            count += diff
        return count
    


s = Solution()
print(s.count_distinct_password_dp2('abaa'))
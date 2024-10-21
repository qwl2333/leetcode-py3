# lc 71
class Solution:
    # Time O(n), space O(n)
    # 需要注意 /../../ 还是 根文件夹 /
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur_dir = ''
        for c in path + '/': # 加上 / 是为了防止之前的路径结尾没有/就会少放一个dir进入stack
            if c != '/':
                cur_dir += c
            else: # c = '/'
                if cur_dir == '':
                    continue
                elif cur_dir == '.':
                    cur_dir = ''
                elif cur_dir == '..':
                    if stack:
                        stack.pop()
                    cur_dir = ''
                else: # cur_dir is a real directory could be a, AAA, ...A, etc
                    stack.append(cur_dir)
                    cur_dir = ''

        res = ''
        while stack:
            res = stack.pop() + res
            res = '/' + res
        return res if res != '' else '/'

s = Solution()
print(s.simplifyPath('/home/user/Documents/../Pictures')) # /..a
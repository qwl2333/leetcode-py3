# lc 691
from collections import deque, Counter
class Solution:
    # https://www.youtube.com/watch?v=OuK1ezMdA-w&ab_channel=CrackingFAANG
    # dfs + memo
    # Time O(m * 2^n) n - length of target, m - number of stickers
    # Space O(2^n) - space we need for memo + stack
    def minStickersDFS(self, stickers: list[str], target: str) -> int:
        sticker_counts = [Counter(sticker) for sticker in stickers]
        memo = {}

        def dfs(target_str): # min stickers we need to form the target string
            if not target_str:
                return 0
            
            if target_str in memo:
                return memo[target_str]
            
            target_counter = Counter(target_str)
            ans = float('inf')

            for sticker in sticker_counts:
                if target_str[0] not in sticker:
                    continue

                remaining_characters = target_counter - sticker # Counter 相减，只会把被减的target_counter里面和sticker相交的character减去，没交集的不会变，如果target_counter里面freq比sticker的小，也只会被删掉，不会变成负数， like Counter {a:1} - Counter {a:2} = Counter()
                letters = [char * count for char, count in remaining_characters.items()]
                next_target = "".join(letters)

                ans = min(ans, 1 + dfs(next_target))
            
            memo[target_str] = ans
            
            return ans
        
        ans = dfs(target)

        return ans if ans != float('inf') else -1
        

    # 最优解 类似 word ladder 2 思路
    # https://leetcode.cn/problems/stickers-to-spell-word/solutions/1492826/pythonjavajavascriptgo-by-himymben-43ik/
    # BFS solution
    # O(n * m * n) n - length of target, m - number of stickers
    def minStickersBFS(self, stickers: list[str], target: str) -> int:
        def trans(s):
            cnts = Counter()
            for c in s:
                if c in target:
                    cnts[c] += 1
            return cnts

        stickers_transformed = [c for st in stickers if (c:=trans(st))] # 只有和target相关的characters被留下来
        queue = deque([(target, 0)])
        explored = {target}
        while queue:
            cur, step = queue.popleft() # cur可以理解为剩下的target string，只要剩下的target里面有在character和sticker有交集，就说明这个sticker可能可以成为最优解
            if not cur:
                return step
            for sticker in stickers_transformed:
                # 不需要对比cur和sticker里面所有的character的频率
                # cur target string的第一个character如果和sticker有交集，
                # 如果最优解存在，是肯定能在最优解里面找到一个或ticker来消除这个第一个character的
                # 这样可以避免先消除a，再消除b，和先消除b，再消除a的情况，这俩是不同的路径但是消除的都是ab的组合
                if cur[0] in sticker:
                    nxt = cur                 
                    for k, v in sticker.items():
                        nxt = nxt.replace(k, '', v) # O(n)的操作， n is length of target
                    if nxt not in explored:
                        explored.add(nxt)
                        queue.append((nxt, step + 1))
        return -1

s = Solution()
print(s.minStickersBFS(["with","example","science"], "thehat"))
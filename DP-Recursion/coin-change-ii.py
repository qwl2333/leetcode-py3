# lc 518 和 lc 39 非常类似 只是 lc 518是求出所有能组成这个金额的方法数, lc 39是要把能组成这个金额 具体组合打出来
# 只求个数,dp或者memo就可以, 但是要具体路径 就需要backtracking
class Solution:
    """
    【思路推导】
    第一步：如何避免重复组合？
    如果我们像上一题那样先遍历金额再遍历硬币，会算出 [1, 2] 和 [2, 1] 两种情况。
    解决方法：先固定硬币。比如先用硬币 1 把全表扫一遍，再用硬币 2 扫一遍。
    这样保证了硬币只会被按照固定的顺序加入，从而只产生 [1, 2] 这一种组合。

    第二步：状态转移
    dp[i] 表示凑齐金额 i 的方法总数。
    当你加入一个新的硬币 coin 时：
    凑齐 i 元的新方法数 = 原有的方法数 + 凑齐 (i - coin) 元的方法数。
    """

    def change(self, amount: int, coins: list[int]) -> int:
        # 1. 初始化 DP 数组，dp[0] = 1 代表凑齐 0 元有一种方法（什么都不选）
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        # 2. 关键：外层循环遍历硬币（保证硬币使用的顺序性）
        for coin in coins:
            # 3. 内层循环遍历金额
            for i in range(coin, amount + 1):
                # 状态转移：累加方法数
                dp[i] += dp[i - coin]
                
        return dp[amount]

    """
    【复杂度分析】
    - 时间复杂度 (TC): $O(amount * n)$, n 为硬币种类。
    - 空间复杂度 (SC): $O(amount)$，只需一维数组记录金额状态。
    """

    # 下面这个就是加入我要打印出所有组合, 其实就和lc 39 一模一样了
    def change_and_print(self, amount: int, coins: list[int]) -> list[list[int]]:
        res = []      # 存储所有成功的路径
        path = []     # 存储当前正在尝试的路径
        
        # 排序是为了方便剪枝：如果当前硬币太大了，后面的硬币就不用看了
        coins.sort()

        def backtrack(start_index, remain):
            # 1. 基准情况：正好凑齐了
            if remain == 0:
                # 注意：这里要放 path 的拷贝 (path[:])，否则后面 pop 会把结果改掉
                res.append(list(path))
                return
            
            # 2. 遍历选项：从 start_index 开始是为了避免重复组合 (如 [1,2] 和 [2,1])
            for i in range(start_index, len(coins)):
                coin = coins[i]
                
                # 【剪枝】：如果当前硬币已经超过剩余金额，直接收工
                if coin > remain:
                    break
                
                # --- [做选择] ---
                # “加一枚硬币”：放入你的口袋
                path.append(coin)
                
                # --- [进入下一层] ---
                # 传入 i 而不是 i + 1，是因为硬币可以无限次使用
                backtrack(i, remain - coin)
                
                # --- [撤销选择] ---
                # “吐出一枚硬币”：从口袋拿出来，回到之前的状态，准备试下一个硬币
                path.pop()
        
        backtrack(0, amount)
        return res

# 测试一下
# sol = Solution()
# print(sol.change_and_print(5, [1, 2, 5]))
# 输出: [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 2, 2], [5]]
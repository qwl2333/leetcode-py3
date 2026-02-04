# lc 322
class Solution:
    """
    【思路推导】
    第一步：为什么不用贪心？
    硬币 [1, 3, 4]，目标 6。贪心选 4+1+1 (3枚)，最优选 3+3 (2枚)。
    结论：局部最优不代表全局最优，需遍历所有组合。

    第二步：状态转移 (迭代视角)
    我们定义一个数组 dp, 
    其中 dp[i] 表示凑齐金额 i 所需的最少硬币数。
    如果我们要凑金额 i: 假设我们最后选的一枚硬币面值是 coin。
    那么我们需要的最少硬币数就是: 凑齐 i - coin 的最少硬币数 dp[i - coin] + 这一枚硬币。我们要从所有面值的硬币中，选出那个能让硬币总数最少的。
    dp[i] = min(dp[i], dp[i - coin] + 1)
    即：想要凑齐 i 元，可以看凑齐 (i - 某个硬币面值) 元的最少数量，再加上那一枚硬币。

    【复杂度分析】
    - 时间复杂度 (TC): O(amount * n)
      我们需要填满长度为 amount 的数组，每一格都要遍历 n 个硬币。
    - 空间复杂度 (SC): O(amount)
      需要一个大小为 amount + 1 的数组来存储中间状态。
    """

    def coin_change(self, coins: list[int], amount: int) -> int:
        # 初始化 DP 数组，dp[i] 表示 凑齐 i 需要的最少硬币个数
        # amount + 1 长度是因为 i的范围是[0, amount]
        dp = [float('inf') for _ in range(amount + 1)] # 这里用 amount+1 代替 float('inf') 也行
                                                       # 因为数额 amount 最多需要 amount 个 1 硬币永远用不了 amount+1 个硬币
        dp[0] = 0  # 基础状态：凑 0 元需 0 枚硬币
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1


    # 【思路推导】
    # 第一步：为什么用记忆化？
    # 凑 11 元选了 5 元剩下 6 元；选了 1 元剩下 10 元。
    # 如果不记录，10 元拆解过程中还会再次遇到 6 元，造成海量重复计算。
    #
    # 第二步：状态转移 (递归视角)
    # dfs(rem) = min(dfs(rem - coin) + 1)
    # 自顶向下拆解问题，直到金额为 0。

    # - 时间复杂度 (TC): O(amount * n)
    #   由于记忆化，每个金额状态只会计算一次。每个状态下尝试 n 个硬币
    # - 空间复杂度 (SC): O(amount)
    #   记忆化缓存（Memo）需要 O(amount) 空间；递归栈深度在最坏情况下（全是 1 元硬币）也是 O(amount)

    # 定义递归函数：dfs(rem) 表示凑齐剩余金额 rem 所需的最少硬币数
    def coin_change_memo(self, coins: list[int], amount: int) -> int:
        memo = {}
        def dfs(rem: int) -> int:
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            res = float('inf')
            for coin in coins:
                if rem - coin >= 0:
                    res = min(res, dfs(rem - coin) + 1)

            memo[rem] = res
            return res
        
        final_res = dfs(amount)
        return final_res if final_res != float('inf') else -1
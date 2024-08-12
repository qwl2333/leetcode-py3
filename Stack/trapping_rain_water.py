# lc 42
class Solution:
    # brute force - time O(n^2), space O(1) 花花解法
    # For column i, the rain it can trap:
    # r[i] = min(max[0 ~ i], max[i ~ n - 1]) - h[i]
    # ans = sum(r[i])
    def trap_bf(self, height: list[int]) -> int:
        sum = 0
        n = len(height)
        for i, h in enumerate(height):
            left_max = self.get_max(height, 0, i)
            right_max = self.get_max(height, i, n - 1) # 为啥要左右都包含i，这样可以保证返回值一定>=height[i]，不会漏掉当前h就是左/右最高的情况，当然这种情况意味着0雨水
            sum += min(left_max, right_max) - h
        return sum
    
    def get_max(self, height: list[int], start: int, end: int) -> int:
        max_h = 0
        for i in range(start, end + 1):
            max_h = max(max_h, height[i])

        return max_h

    # 用 dp 优化 brute force - time O(n), space O(n)
    def trap_dp(self, height: list[int]) -> int:
        sum = 0
        n = len(height)
        lmax = [0] * n # lmax[i] means [0, i] 最大的height
        rmax = [0] * n # rmax[i] means [i, n - 1]最大的height
        lmax[0] = height[0]
        rmax[n - 1] = height[n - 1]
        for i in range(1, n):
            lmax[i] = max(lmax[i - 1], height[i])
            rmax[n - i - 1] = max(rmax[n - i], height[n - i - 1])
        
        for i in range(n):
            sum += min(lmax(i), rmax(i)) - height[i]
        
        return sum



    # stack sol - time O(n) space O(n)
    def trap(self, height: list[int]) -> int:
        stack = [] # 单调不严格递减
        sum = 0
        for i, h in enumerate(height):
            if not stack:
                stack.append(i)
                continue
            
            while h > height[stack[-1]]:
                top_index = stack.pop()
                lowest = height[top_index]
                if stack:
                    sum += (min(height[stack[-1]], h) - lowest) * (i - stack[-1] - 1)
                else:
                    break

            stack.append(i)
        
        return sum
    
s = Solution()
print(s.trap([1,0,0,2,1,0,1,3,2,1,2,1]))
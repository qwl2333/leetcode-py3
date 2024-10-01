# https://www.fastprep.io/problems/amazon-calculate-median-sum
'''
题目是给n个channel,每个channel至少反一个packet,每个packet只能放一个channel
median of channel就是所有packet的median值
求所有channel最大的sum of median of all channels
packets = [1,2,3,4,5] n = 3
greedy:
channel 1: 5
channel 2: 4
channel 3: 1,2,3
sum = 5 + 4 + 2
'''
class Solution:
    def calculateMedianSum(self, packets: list[int], n: int) -> int:
        packets.sort(reverse = True) # 5,4,3,2,1,0
        m = len(packets)
        ans = 0
        for i in range(n - 1):
            ans += packets[i] # 5 + 3

        if (m - n + 1) % 2 == 1:
            ans += packets[n - 1 + (m - n + 1) // 2] # 正好在中点
        else:
            second = packets[n - 1 + (m - n + 1) // 2]
            first = packets[n - 1 + (m - n + 1) // 2 - 1]
            tmp = (second + first + 1) // 2 # 往上round up
            ans += tmp
        return ans

s = Solution()
print(s.calculateMedianSum([5, 2, 2, 1, 5, 3], 2))
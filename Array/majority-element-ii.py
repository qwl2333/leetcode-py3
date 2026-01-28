# lc 229
class Solution:
    # 正常做法肯定是用dict记录数字出现的次数
    # 这个做法是单纯选两个不同的candidate，每次出现第三个不同的就消消乐一下，可以达到space O(1)
    def majorityElement(self, nums: list[int]) -> list[int]:
        if not nums: return []
        
        # 1. 投票阶段
        cand1, count1 = None, 0
        cand2, count2 = None, 0
        
        for n in nums:
            # 情况1：投给候选人1
            if n == cand1:
                count1 += 1
            # 情况2：投给候选人2
            elif n == cand2:
                count2 += 1
            # 情况3：候选人1位子空了，占领它
            elif count1 == 0:
                cand1, count1 = n, 1
            # 情况4：候选人2位子空了，占领它
            elif count2 == 0:
                cand2, count2 = n, 1
            # 情况5：三个数互不相同，同归于尽
            else:
                count1 -= 1
                count2 -= 1
        
        # 2. 验证阶段（回马枪）
        # 投票法只能选出前两名，不代表他们真的及格了
        res = []
        n = len(nums)
        if nums.count(cand1) > n // 3:
            res.append(cand1)
        # 注意：cand2 必须和 cand1 不同才能加进去
        if nums.count(cand2) > n // 3:
            res.append(cand2)
            
        return res
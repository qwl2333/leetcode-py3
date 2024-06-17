# oracle 面试题
'''
Problem Statement
You are given two arrays: energyCosts and points, and an integer initialEnergy.
energyCosts[i] represents the energy required to move from position i to i+1.
point‍‍‌‌‌‌‌‌‍s[i] represents the points you earn at position i, could be positive or negative
You start with initialEnergy.
Your task is to determine the starting index i such that you can maximize the total points you can earn before running out of energy.


相当于求 max subarray of points[]
1. 先把得到energyCosts[]的prefix sum array
2. 求 max subarray of points[], 在这个过程中记录energy cost
3. 记录 max subarray 但 cost < initialEnergy的

ex:

initialEnergy = 10
energyCosts   = [2, 2, 2, 1, 3, 5, 2, 1, 2]
reward_points = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

prefix_sum_cost = [0, 2, 4, 6, 7, 10, 15, 17, 18, 20]

双指针l,r = 0,0
l不动,r走到initial energy用完不够了,就计算一下rewards
然后再走一步l直到r可以移动为止,l移动的过程计算reward,
重复这个过程,知道l,r都到最右
'''
class BallFalling:
    def best_place_to_start_dropping(self, initial_energy: int, energy_cost: list[int], reward_points: list[int]) -> int:
        n = len(energy_cost)
        prefix_rewards = [0 for i in range(n + 1)]
        prefix_rewards[1] = reward_points[0]
        for i in range(2, n + 1):
            prefix_rewards[i] = prefix_rewards[i - 1] + reward_points[i - 1]
        
        l, r = 0, 0
        rewards_sum = -float('inf')
        target_idx = -1
        energy_cost_sum = 0
        while l < n or r < n:
            while l < n and l == r and energy_cost[l] > initial_energy: # 例如inital energe = 2, energy cost[3,3,4,2,100],需要同时移动l,r 直到能量够小球走的位置，如index = 3
                l += 1
                r += 1

            if l == n: # 如果l,r都走到最后了就结束循环 例如inital energe = 1, energy cost[2,3,4,100], 初始energy太少了，只会走到最后跳出循环
                break

            while r < n and energy_cost_sum + energy_cost[r] <= initial_energy: # 这是判断当前的r所在的位置能不能走，如果energy_cost_sum + energy_cost[r] <= initial_energy，意味着小球可以通过r所在位置
                energy_cost_sum += energy_cost[r]
                r += 1
            # 在循环结束后，此时r所在的位置，已经不能再纳入window了，因为energy_cost_sum + energy_cost[r] > initial_energy 能量不够了
            # 需要通过右移l，来shrink window获得更多能量
            # 此时l所在的位置，是准备从window里面排出的下一个元素

            # calculate rewards 紧挨着expand window，此时能量耗尽可以计算rewards
            # 在计算rewards的时候，window应该是最大的expand了，意思就是能量消耗最接近initial energy，再expand就超过了
            # 如何做到的，是因为一开始我们先expand r指针直到消费完所有能量
            # 然后shrink window 通过移动l指针一步，看能不能继续右移r指针来expand window
            # 移动l后如果49行不能继续expand window，那此时也是以l为起点的最大window了，是可以计算rewards的
            rewards_at_cur_window = prefix_rewards[r] - prefix_rewards[l]
            if rewards_at_cur_window > rewards_sum:
                rewards_sum = rewards_at_cur_window
                target_idx = l
            
            # 向左移动l一步，同时更新消耗的能量，移动一步的本质是保证l经过的每一个点都有最大的window来计算rewards
            # 一步过后energy_cost_sum可能小到了可以纳入新的元素了，也就是r所在的位置的元素
            # 所以每次只移动一步，也可能移动一步之后49行仍然无法expand window，没关系，那意味着从l开始已经到了最大的window了，不能再expand因为能量不够了
            # 因为这里会继续shrink window来减少energy cost的总和
            energy_cost_sum -= energy_cost[l]
            l += 1
        
        return (target_idx, rewards_sum)


s = BallFalling()
# print(s.best_place_to_start_dropping(1, [2, 2, 2, 1, 3, 4, 2, 1, 2], [-2, 1, 3, 4, -1, 2, 1, -5, 4]))
print(s.best_place_to_start_dropping(2, [2, 2, 2, 100], [-2, 1, 3, 4]))
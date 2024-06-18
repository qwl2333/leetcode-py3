# lc 621
from collections import deque
from heapq import heappush, heappop
from collections import defaultdict
class Solution:
    # Time 0(N + klogk + Nlogk) N - number of tasks, k - unique tasks
    '''
    Overall Time Complexity: Counting task frequencies: O(N) 
                        Creating the max heap: O(klogk) 
                        Main loop operations (including heap operations): O(Nlogk) WORST CASE the loop runs O(N) times because each task will be processed once

    Space Complexity: Task Frequency Counter O(k) space to store the frequency of each task
                      Max Heap O(k)
                      Cooldown Queue - In the worst case, the queue could store up to N elements if each task is unique and the cooldown period is very long. However, typically it will store a fraction of N elements depending on the value of n
                      = O(N + k)
    '''
    def leastInterval(self, tasks, n):
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        max_q = []
        for task, f in freq.items():
            heappush(max_q, (-f, task))
        
        cool_down_queue = deque()
        time = 0
        while max_q or cool_down_queue:
            while cool_down_queue and cool_down_queue[0][1] == time:
                task, _time_out_of_queue, freq = cool_down_queue.popleft()
                heappush(max_q, (-freq, task))
            
            if max_q:
                neg_f, task = heappop(max_q)
                freq = -neg_f
                freq -= 1
                if freq > 0:
                    cool_down_queue.append((task, time + n + 1, freq))
            
            time += 1
        
        return time
    
    def leastInterval2(self, tasks: list[str], n: int) -> int:
        freq = defaultdict(int)
        max_freq = -float('inf')
        for task in tasks:
            freq[task] += 1
            max_freq = max(max_freq, freq[task])
        max_freq_count = 0
        for v in freq.values():
            if v == max_freq:
                max_freq_count += 1
        
        ans = (max_freq - 1) * (n + 1) + max_freq_count # 如果需要idle，那这就是总共的步数

        return max(ans, len(tasks)) # 最后结果一定是需要idle vs 不需要idle，选大的那个


s = Solution()
print(s.leastInterval(["A","A","A","B","B","B"], 1))
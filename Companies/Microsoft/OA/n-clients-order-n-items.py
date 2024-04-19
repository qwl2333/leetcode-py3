# There are N clients who have ordered N handmade items. The K-th client ordered exactly one item that takes T[K] hours to make. There is only one employee who makes items for clients, and he/she works in the following manner:

# - Spend 1 hour making the first item.

# - If the item is finished, deliver it

# - If the item is NOT finished, put it after ALL REMAINING ITEMS for further work

# - Employee then works on next item

# What is the total time that clients need to wait for all ordered items?

# Example: T = [3, 1, 2]

# In this example, the 1st item takes 3 hours to make, the 2nd item takes 2 hours, and the 3rd item takes 2 hours. Here is how the employee goes about finishing all items: [1st, 2nd, 3rd, 1st, 3rd, 1st]
from collections import deque
class NClientsOrderNItems:
    # Time O(m) m - sum(time_needed_for_each_item), space - O(len(time_needed_for_each_item)) space for queue
    def total_clients_wait_time(self, time_needed_for_each_item: list[int]) -> int:
        q = deque()
        for time in time_needed_for_each_item:
            q.append(time)

        res = 0
        counter = 0
        while q:
            cur = q.popleft()
            counter += 1
            cur -= 1
            if cur > 0:
                q.append(cur)
            else:
                res += (counter % (10 ** 9))
        
        return res

    
s = NClientsOrderNItems()
print(s.total_clients_wait_time([3,1,2]))
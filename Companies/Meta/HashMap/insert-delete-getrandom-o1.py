# lc 380
import random
class RandomizedSet:

    def __init__(self):
        self.data_idx_map = {}
        self.data = []

    def insert(self, val: int) -> bool:
        if val in self.data_idx_map:
            return False
        self.data.append(val)
        self.data_idx_map[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.data_idx_map:
            return False
        last_idx = len(self.data) - 1
        last_value = self.data[-1]

        idx_to_val = self.data_idx_map[val]

        self.data[last_idx], self.data[idx_to_val] = self.data[idx_to_val], self.data[last_idx]
        self.data_idx_map[last_value] = idx_to_val

        self.data.pop()
        del self.data_idx_map[val]

        return True

    def getRandom(self) -> int:
        size = len(self.data)
        rd_idx = random.randint(0, size - 1)
        return self.data[rd_idx]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.remove(0)
param_2 = obj.remove(0)
param_3 = obj.insert(0)
param_4 = obj.getRandom()
param_5 = obj.remove(0)
param_6 = obj.insert(0)
print(param_6)
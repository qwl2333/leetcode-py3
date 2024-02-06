# lc 981
class TimeMap:

    def __init__(self):
        self.store: dict[str, list[tuple]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        new_value = (timestamp, value)
        if key in self.store:
            self.store[key].append(new_value)
        else:
            self.store[key] = [new_value]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''
        else:
            values = self.store[key]
            return self.find_last_smaller_or_equal_then_target(values, timestamp)

    def find_last_smaller_or_equal_then_target(self, values: list[tuple], target: int) -> str:
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            mid_timestamp = values[mid][0]
            if mid_timestamp == target:
                return values[mid][1]
            elif mid_timestamp > target:
                r = mid - 1
            else:
                l = mid + 1

        # 关于return r 还是 l，可以试试看在 lc 704里面跑一下例子就明白了
        if r >= 0:
            return values[r][1]
        else:
            return ''



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
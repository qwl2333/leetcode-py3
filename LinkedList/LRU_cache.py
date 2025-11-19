# lc 146
# 难点在要记得一开始给head和tail一个初始值Node(-1, -1)
# 避免了在remove node时要判断这个node前面还有没有节点，或者后面还有没有节点
# 如果前面或者后面没节点了，就不能直接把当前node的前面和后面相连了
# 不过有了dummy的head和tail之后可以保证永远前后有节点，就不用担心这个问题了

# 第二个难点是记得append node的时候要更新self.map
# 如果超了capacity pop from map的时候也要更新self.map
class Node:
    def __init__(self, key: int, val: int):
        self.key = key # key是必须的，因为在超了capacity，del key from cache时，使用的是 self.cache.pop(self.head.next.key)
        self.val = val
        self.prev: 'None' = None
        self.next: 'None' = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # int -> Node
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def delete_node(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def append_to_tail(self, node: Node):
        prev_tail = self.tail.prev
        prev_tail.next = node
        node.prev = prev_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return  -1
        node = self.cache[key]
        self.delete_node(node)
        self.append_to_tail(node)
        return node.val

    def put(self, key: int, val: int):
        if key not in self.cache:
            new_node = Node(key, val)
            self.append_to_tail(new_node)
            self.cache[key] = new_node
            if len(self.cache) > self.capacity:
                self.cache.pop(self.head.next.key)
                self.delete_node(self.head.next)
        else:
            self.get(key)
            self.tail.prev.val = val
            



        


# Your LRUCache object will be instantiated and called as such:
obj = LRUCache(2)
obj.put(1, 0)
obj.put(2, 2)
param_1 = obj.get(1)
obj.put(3, 3)
param_2 = obj.get(2)
obj.put(4, 4)
param_3 = obj.get(1)
param_4 = obj.get(3)
param_5 = obj.get(4)
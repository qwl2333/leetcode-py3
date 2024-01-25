class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove_node(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        node.prev = None
        node.next = None
    
    def append_node(self, node: Node) -> None:
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.remove_node(node)
            self.append_node(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self.map:
            self.remove_node(self.map[key])
        self.append_node(new_node)
        self.map[key] = new_node
        if len(self.map) > self.capacity:
            del self.map[self.head.next.key]
            self.remove_node(self.head.next)
            



        


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
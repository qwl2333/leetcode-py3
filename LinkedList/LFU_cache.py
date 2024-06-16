# lc 460
class Node:
    def __init__(self, key, value):
        self.key = key # evicted node need to delete using this key from key_to_node
        self.value = value # get method need to return value
        self.freq = 1 # we could remove this in the Node but that requires adding more parameter for _update_freq

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0 # need this when we update min_freq

    def append(self, new_node):
        last_node = self.tail.prev
        new_node.next = last_node.next
        new_node.prev = last_node
        last_node.next.prev = new_node
        last_node.next = new_node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def popleft(self):
        if self.size == 0:
            return None
        first_node = self.head.next
        self.remove(first_node)
        return first_node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_node = {}
        self.freq_to_list = {} # freq to dll

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        node = self.key_to_node[key]
        self._update_freq(node, node.value)
        return node.value
    
    def _update_freq(self, node: Node, value: int):
        freq = node.freq
        dll = self.freq_to_list[freq]
        dll.remove(node)
        if freq == self.min_freq and dll.size == 0: # current dll for min freq has run out of nodes, need to update min req
            self.min_freq += 1
        new_freq = freq + 1
        if new_freq not in self.freq_to_list:
            self.freq_to_list[new_freq] = DoublyLinkedList()
        new_dll = self.freq_to_list[new_freq]
        node.freq += 1
        node.value = value
        new_dll.append(node)

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._update_freq(node, value)
        else:
            if len(self.key_to_node) == self.capacity:
                dll_for_min_freq = self.freq_to_list[self.min_freq]
                evicted_node = dll_for_min_freq.popleft()
                del self.key_to_node[evicted_node.key]
            new_node = Node(key, value)
            self.key_to_node[key] = new_node
            if 1 not in self.freq_to_list:
                self.freq_to_list[1] = DoublyLinkedList()
            dll_for_one = self.freq_to_list[1]
            dll_for_one.append(new_node)
            self.min_freq = 1



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
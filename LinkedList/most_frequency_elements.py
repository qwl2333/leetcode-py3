# 类似 lc460 LFU
# https://www.1point3acres.com/bbs/thread-1069852-1-1.html
class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_after(self, new_node, node): # insert new node after node
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

class FrequencyClass:
    def __init__(self):
        self.key_to_freq = {}
        self.freq_to_node = {}
        self.dll = DoublyLinkedList()

    def increase_freq(self, key):
        if key in self.key_to_freq:
            current_freq = self.key_to_freq[key]
            current_node = self.freq_to_node[current_freq]
            next_node = self._get_or_create_node(current_freq + 1)
            if current_node.next != next_node:
                self.dll.insert_after(next_node, current_node)

            current_node.keys.remove(key)
            next_node.keys.add(key)
            self.key_to_freq[key] += 1

            if not current_node.keys:
                self.dll.remove(current_node)
                del self.freq_to_node[current_freq]
        else:
            self.key_to_freq[key] = 1
            current_node = self._get_or_create_node(1)
            if self.dll.head.next != current_node:
                self.dll.insert_after(current_node, self.dll.head)
            current_node.keys.add(key)


    def _get_or_create_node(self, freq):
        if freq not in self.freq_to_node:
            new_node = Node(freq)
            self.freq_to_node[freq] = new_node
        return self.freq_to_node[freq]

    def decrease_freq(self, key):
        if key in self.key_to_freq:
            current_freq = self.key_to_freq[key]
            current_node = self.freq_to_node[current_freq]
            current_node.keys.remove(key)

            if current_freq > 1:
                prev_node = self._get_or_create_node(current_freq - 1)
                if current_node.prev != prev_node:
                    self.dll.insert_after(prev_node, current_node.prev)
                prev_node.keys.add(key)
                self.key_to_freq[key] -= 1
            else:
                del self.key_to_freq[key]

            if not current_node.keys:
                self.dll.remove(current_node)
                del self.freq_to_node[current_freq]

    def key_with_max_frequency(self):
        if self.dll.tail.prev == self.dll.head:
            return None
        return list(self.dll.tail.prev.keys)

    def key_with_min_frequency(self):
        if self.dll.head.next == self.dll.tail:
            return None
        return list(self.dll.head.next.keys)

fc = FrequencyClass()
fc.increase_freq("a")
fc.increase_freq("a")
fc.increase_freq("b")
fc.increase_freq("c")
fc.increase_freq("b")
fc.increase_freq("b")
print(fc.key_with_max_frequency())  # Output: "b"
print(fc.key_with_min_frequency())  # Output: "c"
fc.decrease_freq("b")
print(fc.key_with_max_frequency())  # Output: "b", "a"
print(fc.key_with_min_frequency())  # Output: "c"
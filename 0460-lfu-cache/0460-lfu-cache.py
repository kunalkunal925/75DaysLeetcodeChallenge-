from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(0, 0) # Dummy head
        self.tail = Node(0, 0) # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_tail(self):
        if self.size == 0: return None
        node = self.tail.prev
        self.remove_node(node)
        return node

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.node_map = {} # key -> node
        self.freq_map = defaultdict(DoublyLinkedList) # freq -> DoublyLinkedList

    def _update_freq(self, node):
        # Remove from current frequency list
        freq = node.freq
        self.freq_map[freq].remove_node(node)
        
        # If the list is empty and it was the min_freq, increment min_freq
        if self.freq_map[freq].size == 0 and freq == self.min_freq:
            self.min_freq += 1
        
        # Increment freq and add to new frequency list
        node.freq += 1
        self.freq_map[node.freq].add_to_head(node)

    def get(self, key):
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self._update_freq(node)
        return node.val

    def put(self, key, value):
        if self.capacity == 0: return

        if key in self.node_map:
            node = self.node_map[key]
            node.val = value
            self._update_freq(node)
        else:
            if self.size == self.capacity:
                # Evict the LRU node from the min_freq list
                lru_node = self.freq_map[self.min_freq].remove_tail()
                del self.node_map[lru_node.key]
                self.size -= 1
            
            new_node = Node(key, value)
            self.node_map[key] = new_node
            self.freq_map[1].add_to_head(new_node)
            self.min_freq = 1
            self.size += 1
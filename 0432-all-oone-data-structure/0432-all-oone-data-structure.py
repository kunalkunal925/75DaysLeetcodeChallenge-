class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:
    def __init__(self):
        self.nodes = {}  # key -> Node mapping
        self.head = Node(0)  # Dummy head (min)
        self.tail = Node(0)  # Dummy tail (max)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.nodes:
            # Current count 0, moving to count 1
            if self.head.next.count != 1:
                self._add_node_after(Node(1), self.head)
            self.head.next.keys.add(key)
            self.nodes[key] = self.head.next
        else:
            cur_node = self.nodes[key]
            next_count = cur_node.count + 1
            if cur_node.next.count != next_count:
                self._add_node_after(Node(next_count), cur_node)
            cur_node.next.keys.add(key)
            self.nodes[key] = cur_node.next
            cur_node.keys.remove(key)
            if not cur_node.keys:
                self._remove_node(cur_node)

    def dec(self, key: str) -> None:
        cur_node = self.nodes[key]
        if cur_node.count == 1:
            del self.nodes[key]
        else:
            prev_count = cur_node.count - 1
            if cur_node.prev.count != prev_count:
                # Add node before current node manually or using helper
                new_node = Node(prev_count)
                new_node.next = cur_node
                new_node.prev = cur_node.prev
                cur_node.prev.next = new_node
                cur_node.prev = new_node
            cur_node.prev.keys.add(key)
            self.nodes[key] = cur_node.prev
        
        cur_node.keys.remove(key)
        if not cur_node.keys:
            self._remove_node(cur_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        # Return any key from the set
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))
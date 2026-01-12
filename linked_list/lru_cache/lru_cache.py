
class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None


class LRUCache:  # LeetCode Q.146.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache: dict[int, Node] = dict()  # Value: each key's node.

        self.head, self.tail = Node(-1, -1), Node(-1, -1)  # Initiate head and tail.
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _add(self, node: Node) -> None:  # Insert node next to head.
        next_node = self.head.next
        node.next = next_node
        next_node.prev = node

        self.head.next = node
        node.prev = self.head
    
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        
        node = self.cache[key]
        self._remove(node)

        self._add(node)
        self.cache.update({key: self.head.next})  # Node property has changed.
        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():  # New key coming.
            if len(self.cache) == self.capacity:  # Capacity is full.
                removed_key = self.tail.prev.key
                del self.cache[removed_key]
                self._remove(self.tail.prev)
        
        else:  # Remove already existing node from current spot.
            self._remove(self.cache[key])
        
        node = Node(key, value)
        self._add(node)
        self.cache.update({key: node})

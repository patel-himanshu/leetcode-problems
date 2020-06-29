# Question: https://leetcode.com/explore/challenge/card/30-day-leetcoding-challenge/531/week-4/3309/

"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, 
it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Example:
    LRUCache cache = new LRUCache( 2 /* capacity */ );

    cache.put(1, 1);
    cache.put(2, 2);
    cache.get(1);       // returns 1
    cache.put(3, 3);    // evicts key 2
    cache.get(2);       // returns -1 (not found)
    cache.put(4, 4);    // evicts key 1
    cache.get(1);       // returns -1 (not found)
    cache.get(3);       // returns 3
    cache.get(4);       // returns 4
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.all_keys = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.all_keys:
            node = self.all_keys[key]
            self.remove_from_dict(node)
            self.insert_at_head(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.all_keys:
            node = self.all_keys[key]
            self.remove_from_dict(node)
            node.value = value
        else:
            if len(self.all_keys) >= self.capacity:
                self.remove_from_tail()
            node = Node(key, value)
            self.all_keys[key] = node
        
        self.insert_at_head(node)

    def remove_from_dict(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def insert_at_head(self, node):
        node_head_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node_head_next.prev = node
        node.next = node_head_next
        
    def remove_from_tail(self):
        if not len(self.all_keys): return
        node_tail = self.tail.prev
        del self.all_keys[node_tail.key]
        self.remove_from_dict(node_tail)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
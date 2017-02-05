import unittest


class Node(object):
    def __init__(self, v):
        self.v = v
        self.next_node = None
        self.prev_node = None


class LinkedList(object):
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def add_node_to_head(self, node):
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            old_head = self.head
            self.head = node
            node.next_node = old_head
            old_head.prev_node = node

    def get_oldest_key(self):
        if self.is_empty():
            return None
        else:
            return self.tail.v

    def remove_tail(self):
        pass
        if self.is_empty():
            raise Exception('cache is empty!')
        else:
            prev_tail = self.tail.prev_node
            if prev_tail is None:
                self.head = None
                self.tail = Node
            else:
                prev_tail.next_node = None
                self.tail = prev_tail

    def is_empty(self):
        return self.head is None and self.tail is None


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.cache_size = 0
        self.dict_cache = {}
        self.doubly_linked_list = LinkedList(None, None)
        self.help_dict_for_linked_list = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # get the value
        v = None
        if key in self.dict_cache:
            v = self.dict_cache[key]
            # put the just used node to the head
            pass

        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # check if cache is full
        if self.cache_size >= self.cap:
            # need remove the oldest element
            oldest_key = self.doubly_linked_list.get_oldest_key()
            self.doubly_linked_list.remove_tail()
            self.dict_cache.pop(oldest_key, None)

        self.dict_cache[key] = value
        # add the key element to the head of linkedlist
        node = Node(key)
        self.help_dict_for_linked_list[key] = node
        self.doubly_linked_list.add_node_to_head(node)
        self.cache_size += 1


class MyTest(unittest.TestCase):
    def test(self):
        lruCache = LRUCache(2)
        lruCache.put(1, 2)
        lruCache.put(2, 3)
        lruCache.put(3, 4)

        self.assertIsNone(lruCache.get(1))
        self.assertEqual(lruCache.get(2), 3)
        self.assertEqual(lruCache.get(3), 4)

        lruCache.get(2)
        lruCache.put(4, 6)
        self.assertIsNotNone(lruCache.get(2))
        self.assertIsNotNone(lruCache.get(4))
        self.assertIsNone(lruCache.get(3))


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    print 'Hello World!'
    unittest.main()

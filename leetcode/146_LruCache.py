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

    def move_node_to_head(self, node):
        # firstly remove it from original place
        prev_node = node.prev_node
        next_node = node.next_node
        if prev_node is not None:
            prev_node.next_node = next_node
        else:
            # it is the head, no need to move
            return

        if next_node is not None:
            next_node.prev_node = prev_node
        else:
            # it is the tail, need to update the tail.
            self.tail = prev_node

        # Update the prev_node, it is the indicator of if it is a head node.
        node.prev_node = None

        self.add_node_to_head(node)

    def remove_tail(self):
        if self.is_empty():
            raise Exception('cache is empty!')
        else:
            prev_tail = self.tail.prev_node
            if prev_tail is None:
                self.head = None
                self.tail = None
            else:
                prev_tail.next_node = None
                self.tail.prev_node = None
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
        v = -1
        if key in self.dict_cache:
            v = self.dict_cache[key]
            # put the just used node to the head
            node = self.help_dict_for_linked_list[key]
            self.doubly_linked_list.move_node_to_head(node)
        return v

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict_cache:
            # update the value
            self.dict_cache[key] = value
            # Move the key node to head
            key_node = self.help_dict_for_linked_list[key]
            self.doubly_linked_list.move_node_to_head(key_node)
        else:
            # check if cache is full
            if self.cache_size >= self.cap:

                # need remove the oldest element
                oldest_key = self.doubly_linked_list.get_oldest_key()
                self.doubly_linked_list.remove_tail()

                # Remove it from cache
                self.dict_cache.pop(oldest_key, None)

                # Remove it from helper dict
                self.help_dict_for_linked_list.pop(oldest_key, None)

                # Cache size update
                self.cache_size -= 1

            self.dict_cache[key] = value
            # add the key element to the head of linkedlist
            node = Node(key)
            self.help_dict_for_linked_list[key] = node
            self.doubly_linked_list.add_node_to_head(node)
            self.cache_size += 1


class MyTest(unittest.TestCase):
    def test_my_cases(self):
        lru_cache = LRUCache(2)
        lru_cache.put(1, 2)
        lru_cache.put(2, 3)
        lru_cache.put(3, 4)

        self.assertEqual(-1, lru_cache.get(1))
        self.assertEqual(lru_cache.get(2), 3)
        self.assertEqual(lru_cache.get(3), 4)

        lru_cache.get(2)
        lru_cache.put(4, 6)
        self.assertIsNotNone(lru_cache.get(2))
        self.assertIsNotNone(lru_cache.get(4))
        self.assertEqual(-1, lru_cache.get(3))

    def test_cases_in_question(self):
        cache = LRUCache(2);

        cache.put(1, 1)
        cache.put(2, 2)
        # return  1
        self.assertEqual(1, cache.get(1))

        # evict   key   2
        cache.put(3, 3)

        # returns - 1(not found)
        self.assertEqual(-1, cache.get(2))

        # evicts key 1
        cache.put(4, 4)

        # returns - 1(not found)
        self.assertEqual(-1, cache.get(1))

        self.assertEqual(3, cache.get(3))
        self.assertEqual(4, cache.get(4))

    def test_cases_for_the_first_error(self):
        #[[1],[2,1],[2],[3,2],[2],[3]]
        # Reason: typo. None -> Node wrongly.
        cache = LRUCache(1)
        cache.put(2, 1)
        self.assertEqual(1, cache.get(2))
        cache.put(3, 2)
        self.assertEqual(-1, cache.get(2))
        self.assertEqual(2, cache.get(3))

    def test_cases_for_the_second_error(self):
        # Reason: not handle the case: update the value of existed key.
        # [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]] .Wrong answer
        # Output:
        # [null, -1, null, -1, null, null, 2, -1]
        # Expected:
        # [null, -1, null, -1, null, null, 2, 6]
        cache = LRUCache(2)
        self.assertEqual(-1, cache.get(1))
        cache.put(2, 6)
        self.assertEqual(-1, cache.get(1))
        cache.put(1, 5)
        cache.put(1, 2)
        self.assertEqual(2, cache.get(1))
        self.assertEqual(6, cache.get(2))

    def test_case_for_the_third_error(self):
        # Reason: forgot to update the prev_node  when move the node to the head.
        # Search the line 'node.prev_node = None'
        cache = LRUCache(10)

        # [10:13]
        cache.put(10, 13)

        # [3:17, 10:13]
        cache.put(3, 17)

        # [6:11, 3:17, 10:13]
        cache.put(6, 11)

        # [10:5, 6:11, 3:17]
        cache.put(10, 5)

        # [9:10, 10:5, 6:11, 3:17]
        cache.put(9, 10)

        #
        self.assertEqual(-1, cache.get(13))

        # [2:19, 9:10, 10:5, 6:11, 3:17]
        cache.put(2, 19)

        # [2:19, 9:10, 10:5, 6:11, 3:17]
        self.assertEqual(19, cache.get(2))

        # [3:17, 2:19, 9:10, 10:5, 6:11]
        self.assertEqual(17, cache.get(3))

        # [5:25, 3:17, 2:19, 9:10, 10:5, 6:11]
        cache.put(5, 25)

        # [5:25, 3:17, 2:19, 9:10, 10:5, 6:11]
        self.assertEqual(-1, cache.get(8))

        # [9:22, 5:25, 3:17, 2:19, 10:5, 6:11]
        cache.put(9, 22)

        # [5:5, 9:22, 3:17, 2:19, 10:5, 6:11]
        cache.put(5, 5)

        # [1:30, 5:5, 9:22, 3:17, 2:19, 10:5, 6:11]
        cache.put(1, 30)

        self.assertEqual(-1, cache.get(11))

        # [9:12, 1:30, 5:5, 3:17, 2:19, 10:5, 6:11]
        cache.put(9, 12)

        self.assertEqual(-1, cache.get(7))

        # [5:5, 9:12, 1:30,3:17, 2:19, 10:5, 6:11]
        self.assertEqual(5, cache.get(5))

        self.assertEqual(-1, cache.get(8))

        # [9:12, 5:5, 1:30,3:17, 2:19, 10:5, 6:11]
        self.assertEqual(12, cache.get(9))

        # [4:30, 9:12, 5:5, 1:30,3:17, 2:19, 10:5, 6:11]
        cache.put(4, 30)

        # [9:3, 4:30, 5:5, 1:30,3:17, 2:19, 10:5, 6:11]
        cache.put(9, 3)

        self.assertEqual(3, cache.get(9))

        # [10:5, 9:3, 4:30, 5:5, 1:30,3:17, 2:19, 6:11]
        self.assertEqual(5, cache.get(10))
        self.assertEqual(5, cache.get(10))

        # [6:14, 10:5, 9:3, 4:30, 5:5, 1:30,3:17, 2:19]
        cache.put(6, 14)

        # [3:1, 6:14, 10:5, 9:3, 4:30, 5:5, 1:30,3:17, 2:19]
        cache.put(3, 1)

        # [3:1, 6:14, 10:5, 9:3, 4:30, 5:5, 1:30,3:17, 2:19]
        self.assertEqual(1,cache.get(3))

        # [10:11, 3:1, 6:14, 10:5, 4:30, 5:5, 1:30, 3:17, 2:19]
        cache.put(10, 11)

        #
        self.assertEqual(-1, cache.get(8))

        # [2:14, 10:11, 3:1, 6:14, 10:5, 4:30, 5:5, 1:30, 3:17]
        cache.put(2, 14)

        # [1:30, 2:14, 10:11, 3:1, 6:14, 10:5, 4:30, 5:5, 3:17]
        self.assertEqual(30, cache.get(1))

        # [5:5, 1:30, 2:14, 10:11, 3:1, 6:14, 10:5, 4:30, 3:17]
        self.assertEqual(5, cache.get(5))

        # [4:30, 5:5, 1:30, 2:14, 10:11, 3:1, 6:14, 10:5, 3:17]
        self.assertEqual(30, cache.get(4))

        # [11:4, 4:30, 5:5, 1:30, 2:14, 10:11, 3:1, 6:14, 10:5, 3:17]
        cache.put(11, 4)

        # [12:24, 11:4, 4:30, 5:5, 1:30, 2:14, 10:11, 3:1, 6:14, 10:5]
        cache.put(12, 24)

        # [5: 18, 12:24, 11:4, 4:30, 1:30, 2:14, 10:11, 3:1, 6:14, 10:5]
        cache.put(5, 18)

        self.assertEqual(-1, cache.get(13))

        # [7:23, 5: 18, 12:24, 11:4, 4:30, 1:30, 2:14, 10:11, 3:1, 6:14]
        cache.put(7, 23)

        self.assertEqual(-1, cache.get(8))

        # [12:24, 7:23, 5: 18, 11:4, 4:30, 1:30, 2:14, 10:11, 3:1, 6:14]
        self.assertEqual(24, cache.get(12))

        # [3:27, 12:24, 7:23, 5: 18, 11:4, 4:30, 1:30, 2:14, 10:11, 6:14]
        cache.put(3, 27)

        # [2:12, 3:27, 12:24, 7:23, 5: 18, 11:4, 4:30, 1:30, 10:11, 6:14]
        cache.put(2, 12)

        # [5:18, 2:12, 3:27, 12:24, 7:23, 11:4, 4:30, 1:30, 10:11, 6:14]
        self.assertEqual(18, cache.get(5))

        # [2:9, 5:18, 3:27, 12:24, 7:23, 11:4, 4:30, 1:30, 10:11, 6:14]
        cache.put(2, 9)

        # [13:4, 2:9, 5:18, 3:27, 12:24, 7:23, 11:4, 4:30, 1:30, 10:11]
        cache.put(13, 4)

        # [8:18, 13:4, 2:9, 5:18, 3:27, 12:24, 7:23, 11:4, 4:30, 1:30]
        cache.put(8, 18)

        # [1:7, 8:18, 13:4, 2:9, 5:18, 3:27, 12:24, 7:23, 11:4, 4:30]
        cache.put(1, 7)
        self.assertEqual(-1, cache.get(6))





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == '__main__':
    print 'Hello World!'
    unittest.main()

import unittest


'''
2017/01/19:
    Initial version is OK. Debugging many times.
    Result:
        beat 7% in python
    Issues:
    1. When out of loop (for), forgot to update the current vars.
    2. In some 'if'/'else' conditions, forgot to update the current vars.
    3. one offset error. Use range(30, 0, -1), should be range(30, -1, -1)

    Learned:
    1. mask. Will help you remember i & (1<<j) visually.
    2. Use (left, right) to print tree easily. And use notpad++ to see the tree, since notepad++ will
        hightlight the '(' pair.

'''

class TrieNode(object):
    def __init__(self):
        self.children = [None, None]

    def is_leaf(self):
        return self.children[0] is None and self.children[1] is None

    def to_str(self):
        my_str = '('
        if self.children[0] is not None:
            my_str += '0:' + self.children[0].to_str()
        else:
            my_str += 'None'
        my_str += ','
        if self.children[1] is not None:
            my_str += '1:' + self.children[1].to_str()
        else:
            my_str += 'None'

        my_str += ')'
        return my_str


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_xor = -1

        # Init the trie
        root = TrieNode()
        current_node = root
        for i in nums:
            # bit by bit
            # for bit 32 -> 1
            #   try to find is there is such tree path; if not insert it.
            for j in range(30, -1, -1):
                is_zero = i & (1 << j)
                if is_zero == 0:
                    # the jth bit is 0
                    if current_node.children[0] is not None:
                        current_node = current_node.children[0]
                    else:
                        child_node = TrieNode()
                        current_node.children[0] = child_node
                        current_node = child_node
                else:
                    # the jth bit is 1
                    if current_node.children[1] is not None:
                        current_node = current_node.children[1]
                    else:
                        child_node = TrieNode()
                        current_node.children[1] = child_node
                        current_node = child_node
            current_node = root

        # find the max xor
        current_node = root
        for i in nums:
            # check bit one by one from left to right.
            # if can find !bit in trie, add the value to current record.
            # else continue to next.
            # after bits check, try to update the max xor.
            xor_value = 0
            for j in range(30, -1, -1):
                mask = 1 << j
                is_zero = i & mask
                child_nodes = current_node.children
                if is_zero == 0:
                    # Check if 1
                    if child_nodes[1] is not None:
                        xor_value += mask
                        current_node = child_nodes[1]
                    else:
                        current_node = child_nodes[0]
                else:
                    if child_nodes[0] is not None:
                        xor_value += mask
                        current_node = child_nodes[0]
                    else:
                        current_node = child_nodes[1]

            current_node = root
            if xor_value > max_xor:
                max_xor = xor_value

        return max_xor


class MyTest(unittest.TestCase):
    def test(self):
        solution = Solution()
        self.assertEqual(0, solution.findMaximumXOR([1, 1]))
        self.assertEqual(28, solution.findMaximumXOR([3, 10, 5, 25, 2, 8]))
        self.assertEqual(6, solution.findMaximumXOR([2, 4]))


if __name__ == '__main__':
    unittest.main()

import unittest


class Solution(object):
    def countBits(self, num):
        """
        Result: beats 50%, 57%, 35%, 95%. Leetcode judge is not stable.
        The world of binary
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]

        ret = [0] * (num + 1)
        for i in xrange(num + 1):
            ret[i] = ret[i >> 1] + (i & 1)
        return ret


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        ret = s.countBits(0)
        self.assertEqual([0], ret)

        ret = s.countBits(1)
        self.assertEqual([0, 1], ret)

        ret = s.countBits(2)
        self.assertEqual([0, 1, 1], ret)

        ret = s.countBits(3)
        self.assertEqual([0, 1, 1, 2], ret)


if __name__ == '__main__':
    unittest.main()

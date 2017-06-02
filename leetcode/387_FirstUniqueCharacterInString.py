import unittest

import sys


class Solution(object):
    def firstUniqChar(self, s):
        """
        Score: beats 80%.
        :type s: str
        :rtype: int
        """

        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c] = -1
            else:
                d[c] = i
        ret = sys.maxint
        for k, v in d.items():
            if v != -1 and v < ret:
                ret = v
        return ret if ret != sys.maxint else -1


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(0, s.firstUniqChar("leetcode"))
        self.assertEqual(2, s.firstUniqChar("loveleetcoe"))
        self.assertEqual(0, s.firstUniqChar("qwertyuiop"))
        self.assertEqual(-1, s.firstUniqChar("aaaaaa"))


if __name__ == '__main__':
    unittest.main()

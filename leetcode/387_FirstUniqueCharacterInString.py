class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {}
        for i, c in enumerate(s):
            if c in d:
                d[c].append(i)
            else:
                d[c] = [i]
        ret = -1
        for k, v in d.items():
            if len(v) == 1 and (ret == -1 or v[0] < ret):
                ret = v[0]
        return ret


if __name__ == '__main__':
    s = Solution()

    assert 0 == s.firstUniqChar("leetcode")
    assert 2 == s.firstUniqChar("loveleetcode")

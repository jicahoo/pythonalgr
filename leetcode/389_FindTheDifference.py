class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        n = len(sorted_s)
        res = None
        for i in range(n):
            s_element = sorted_s[i]
            t_element = sorted_t[i]
            if s_element != t_element:
                res = t_element
                break
        if res is None:
            return sorted_t[n]


if __name__ == '__main__':
    s = Solution()
    a = "abcde"
    b = "abcdef"
    print s.findTheDifference(a,b)


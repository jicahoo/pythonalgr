isDone = False
description = "Just completed my test cases."


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        pass


class Test(object):
    def __init__(self, solution):
        self.s = solution

    def test(self, s):
        self.test_zero(s)
        self.test_basic(s)
        self.test_big(s)

    def test_basic(self):
        self.test_unit("1", "1")
        self.test_unit("2", "1")
        self.test_unit("2", "3")
        self.test_unit("3", "5")
        self.test_unit("10", "5")
        self.test_unit("10", "51")
        self.test_unit("10", "600")
        self.test_unit("2345", "74940")

    def test_unit(self, a, b):
        '''
        Only for not very big number
        :param a:
        :param b:
        :return:
        '''
        assert int(a) * int(b) == self.s.multiply(a, b)

    def test_big(self, s):
        assert "9" * 100 == s.multiply("1", "9" * 100)
        assert "9" * 10000 == s.multiply("1", "9" * 10000)

    def test_zero(self, s):
        assert "0" == s.multiply("0", "9" * 10000)
        assert 0 == int(s.multiply("0", "0"))
        assert 0 == int(s.multiply("0", "1"))
        assert 23 == int(s.multiply("01", "023"))


if __name__ == '__main__':
    so = Solution()
    t = Test()
    t.test(so)

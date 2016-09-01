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

    def test(self, s):
        self.test_zero(s)
        self.test_basic(s)
        self.test_big(s)

    def test_basic(self,s):
        assert 1 == int(s.multiply("1","1"))
        assert 2 == int(s.multiply("2", "1"))
        assert 6 == int(s.multiply("2", "3"))
        assert 15 == int(s.multiply("3", "5"))
        assert 50 == int(s.multiply("10", "5"))
        assert 50 == int(s.multiply("10", "51"))
        assert 510 == int(s.multiply("10", "51"))

    def test_big(self, s):
        assert "9"*100 == s.multiply("1", "9"*100)
        assert "9"*10000 == s.multiply("1", "9"*10000)

    def test_zero(self, s):
        assert "0" == s.multiply("0", "9"*10000)
        assert 0 == int(s.multiply("0", "0"))
        assert 0 == int(s.multiply("0", "1"))
        assert 23 == int(s.multiply("01", "023"))


if __name__ == '__main__':
    so = Solution()
    t = Test()
    t.test(so)

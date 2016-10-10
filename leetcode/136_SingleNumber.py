class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Just took part in the Python training provided from Cederic. Learned to use Pythonic style.
        return reduce(lambda x, y: x ^ y, nums, 0)


if __name__ == '__main__':
    s = Solution()
    assert 4 == s.singleNumber([10, 9, 10, 9, 4])
    assert 6 == s.singleNumber([10, 9, 6, 10, 9])
    assert 10 == s.singleNumber([10])


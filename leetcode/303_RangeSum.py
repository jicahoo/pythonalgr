class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = nums
        for i in xrange(1, len(nums)):
            self.nums[i] = self.nums[i-1]+self.nums[i]
        self.nums = self.nums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.nums[j]
        return self.nums[j]-self.nums[i-1]

if __name__ == '__main__':
    n = 10
    l = range(n)
    s = NumArray(l)
    print s.sumRange(0, 0)
    print s.sumRange(0, 1)
    print s.sumRange(n - 1, n - 1)
    print s.sumRange(0, n - 1)
    print s.sumRange(n / 2, n - 1)
    print s.sumRange(0, 9)

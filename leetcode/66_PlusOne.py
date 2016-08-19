class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        jin_wei = 1
        n = len(digits)
        break_early = False
        for i in xrange(n-1, -1, -1):
            if jin_wei == 0:
                break_early = True
                break
            else:
                result = digits[i]+jin_wei
                if result < 10:
                    digits[i] = result
                    jin_wei = 0
                else:
                    rest = result - 10
                    digits[i] = rest
                    jin_wei = 1

        if not break_early and jin_wei != 0:
            digits.insert(0, jin_wei)
        return digits


if __name__ == '__main__':
    s = Solution()
    digits = [1, 3, 4, 5, 5]
    print s.plusOne(digits)
    digits = [9, 9, 9, 9, 9]
    print s.plusOne(digits)
    digits = [9, 9, 1, 9, 9]
    print s.plusOne(digits)
    digits = [0]
    print s.plusOne(digits)
    digits = [1]
    print s.plusOne(digits)
    digits = [9]
    print s.plusOne(digits)











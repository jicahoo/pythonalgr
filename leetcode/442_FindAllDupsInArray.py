import unittest


# Got this solution by myself. Not google anything.
class Solution(object):
    def findDuplicates(self, nums):
        """
        For number i in nums. Add n to nums[i-1]. Then you can use how many n in nums[i-1] to record how many times i repeats
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        # First loop: try to add n.
        for idx, val in enumerate(nums):
            original_val = n if val % n == 0 else val % n
            idx_from_val = original_val - 1
            nums[idx_from_val] += n
        dups = []
        # Scan nums to compute how many times it repeats.
        for idx, val in enumerate(nums):
            if 2 * n < val <= 3 * n:
                dups.append(idx + 1)
        return dups


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        self.assertEqual([1], s.findDuplicates([1, 1]))
        self.assertEqual([], s.findDuplicates([1, 2, 3]))
        self.assertEqual([1, 3], s.findDuplicates([1, 1, 3, 3, 4]))
        self.assertEqual([1, 3], s.findDuplicates([1, 3, 3, 1]))
        self.assertEqual([3], s.findDuplicates([1, 1, 1, 3, 4, 3]))


if __name__ == '__main__':
    unittest.main()

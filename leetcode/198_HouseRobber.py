class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        p = nums[0]
        q = max(nums[0], nums[1])
        lastSelected = False
        last = nums[1]
        if q == nums[1] and (nums[0] != nums[1]):
            lastSelected = True

        i = 2
        while i < len(nums):
            cur = nums[i]

            lastSelected_a = False
            posible_better_choice = q - last + cur
            temp_a = max(q, posible_better_choice)
            if temp_a == posible_better_choice and q != posible_better_choice:
                lastSelected_a = True
            p_a = q
            q_a = temp_a

            temp_b = p + cur
            p_b = q
            q_b = temp_b

            temp_max = max(temp_a, temp_b)
            if temp_a == temp_b:
                p = p_a
                q = q_a
            elif temp_a == temp_max:
                p = p_a
                q = q_a
            else:
                p = p_b
                q = q_b
            last = cur

            i += 1
        return q


if __name__ == '__main__':
    a = Solution()
    print a.rob([2, 3, 2])
    print a.rob([0, 0, 0])
    print a.rob([1, 1, 1])
    print a.rob([1, 1, 1, 2])

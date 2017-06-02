import unittest


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        for c in input:
            print c

    def compute(self, input):
        '''
        Compute next step.
        :param input: [input]
        :return: Intermediate ['', '','']
        '''
        result = [input]
        final_result = []
        while len(result) > 0:
            new_round_result = []
            for res in result:
                if not self.has_operator(res):
                    final_result.append(int(res))
                new_children = self.compute_next_step(res)
                new_round_result += new_children
            result = [ele for ele in new_round_result if self.has_operator(ele)]
            final_result += [int(ele) for ele in new_round_result if not self.has_operator(ele)]
        return final_result

    def compute_next_step(self, expr_str):
        result = []
        for i, v in enumerate(expr_str):
            if self.is_operatoe(v):
                compute_with_next_number = eval(expr_str[:i+2])
                one_road = str(compute_with_next_number) + expr_str[(i+2):]
                # other_road = [expr_str[:i], expr_str[i], expr_str[]]
                break




    def has_operator(self, some_str):
        return '*' in some_str or '+' in some_str or '-' in some_str
    def is_operatoe(self, ch):
        return ch in ('*', '+', '-')


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        expect_result = [-34, -14, -10, -10, 10]
        self.assertEqual(expect_result, s.diffWaysToCompute('2*3-4*5'))

        expect_result = [0, 2]

        self.assertEqual(expect_result, s.diffWaysToCompute('2-1-1'))


if __name__ == '__main__':
    unittest.main()

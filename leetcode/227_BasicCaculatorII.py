import re

'''
0. Tokenize
1. operator priority:
2. computer process (by hand): 1+2*3-5+6 -> Split by '-' or '+'. computer the sub component, linearly compute.
'''


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        operands = re.split('[\+\-]', s)
        operators = [op for op in s if op == '+' or op == '-']
        operators = ["+"] + operators

        # Trim:
        stripped_operands = []
        for operand in operands:
            stripped_operands.append(operand.strip())

        # Handle +*
        n = len(stripped_operands)
        res = 0
        for i in xrange(n):
            operand = stripped_operands[i]
            if '*' in operand or '/' in operand:
                next_operand = self.handle(operand)
            else:
                next_operand = int(operand)
            if operators[i] == "+":
                res += next_operand
            elif operators[i] == "-":
                res -= next_operand
            else:
                raise ValueError("Invalid operator: " + operators[i])
        return res

    def handle(self, token):
        '''
        Caculate * /
        :param token:
        :return: int
        '''

        operands = re.split('[/\*]', token)
        stripped_operands = [operand.strip() for operand in operands]
        operators = [op for op in token if op == '/' or op == '*']
        operators = ["*"] + operators
        n = len(stripped_operands)
        res = 1
        for i in xrange(n):
            next_operand = int(stripped_operands[i])
            if operators[i] == "*":
                res *= next_operand
            elif operators[i] == "/":
                res /= next_operand
            else:
                raise ValueError("Invalid operator: " + operators[i])
        return res


if __name__ == '__main__':
    s = Solution()

    assert 2 == s.calculate("2")
    assert 2 == s.calculate("1+1")
    assert 2 == s.calculate(" 1 +  1 ")
    assert 0 == s.calculate("1-1")
    assert 1 == s.calculate("2-1")
    assert 12 == s.calculate("3*4")
    assert 1 == s.calculate("4/3")
    assert 7 == s.calculate("3+2*2")
    assert 1 == s.calculate(" 3/2 ")
    assert 5 == s.calculate(" 3+5 / 2 ")

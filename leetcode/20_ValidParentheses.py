class Solution(object):
    def isValid(self, s):
        """For now, beat  30%.
        :type s: str
        :rtype: bool
        """
        if s == "":
            return True
        stack = []
        for letter in s:
            if letter in ('{','[','('):
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                element = stack.pop()
                match_a = (letter == '}' and element == '{')
                match_b = (letter == ']' and element == '[')
                match_c = (letter == ')' and element == '(')
                if not (match_a or match_b or match_c):
                    return False
        if len(stack) != 0:
            return False
        else:
            return True


if __name__ == '__main__':
    s = Solution()
    assert not s.isValid("{")
    assert not s.isValid("}")
    assert not s.isValid("[")
    assert not s.isValid("[{(")
    assert not s.isValid("[]{)")
    assert s.isValid("")
    assert s.isValid("[]")
    assert s.isValid("{}")
    assert s.isValid("()")
    assert s.isValid("[]{}()")
    assert s.isValid("{[()]}")
    assert s.isValid("[()][[]]{}()")





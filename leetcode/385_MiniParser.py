"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger(object):
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        if value is None:
            self.element_list = []
            self.is_int = False
        else:
            self.is_int = True
            self.element_int = value

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return self.is_int

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        self.element_list.append(elem)

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        self.is_int = True
        self.element_int = value

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.element_int
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.isInteger():
            return None
        else:
            return self.element_list

    def __str__(self):
        if self.isInteger():
            return str(self.element_int)
        else:
            return str(self.element_list)

    def __repr__(self):
        if self.isInteger():
            return str(self.element_int)
        else:
            return str(self.element_list)


class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: list
        """
        if s[0] == '[':
            # is list
            strs = self.split(s)
            ls = NestedInteger()
            for e in strs:
                if e != '':
                    ls.getList().append(self.deserialize(e))
            return ls
        else:
            # should be a digit
            return NestedInteger(int(s))

    def split(self, s):
        strs = []
        stack = []
        k = 1
        n = len(s)
        for i in xrange(n):
            c = s[i]
            if c == "[":
                stack.append(c)
            elif c == "]":
                stack.pop()
            if c == "," and len(stack) == 1:
                element = s[k:i]
                k = i + 1
                strs.append(element)
        strs.append(s[k:n - 1])
        return strs


class SolutionJichao(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: list
        """
        if s[0] == '[':
            # is list
            strs = self.split(s)
            ls = []
            for e in strs:
                ls.append(self.deserialize(e))
            return ls
        else:
            # should be a digit
            return int(s)

    def split(self, s):
        strs = []
        stack = []
        k = 1
        n = len(s)
        for i in xrange(n):
            c = s[i]
            if c == "[":
                stack.append(c)
            elif c == "]":
                stack.pop()
            if c == "," and len(stack) == 1:
                element = s[k:i]
                k = i + 1
                strs.append(element)
        strs.append(s[k:n - 1])
        return strs


if __name__ == '__main__':
    # s = SolutionJichao()
    s = Solution()
    case_a = "[1,3,4,5]"
    print s.deserialize(case_a)
    case_b = "[1,3,4,[5]]"
    print s.deserialize(case_b)
    case_c = "[-1,3,4,[5]]"
    print s.deserialize(case_c)

    d = [-1, 3, 4, [-5, [1, 333, -444], [4, 5, 6, -9]]]
    case_d = "[-1,3,4,[-5,[1,333,-444],[4,5,6,-9]]]"
    # print s.split(case_d)
    # print s.split("[]")
    print s.deserialize(case_d)
    case_f = "[]"
    print s.deserialize(case_f)

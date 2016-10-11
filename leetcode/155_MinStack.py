import heapq


class MinStackV1(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = []
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        heapq.heappush(self.heap, x)

    def pop(self):
        """
        :rtype: void
        """
        e = self.stack[-1]
        self.stack.pop()
        if e != self.heap[0]:
            self.heap.remove(e)
            heapq.heapify(self.heap)
        else:
            heapq.heappop(self.heap)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.heap[0]

# Below solution is better: best score 60%
import sys
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = sys.maxint

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x < self.min_val:
            self.min_val = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        if len(self.stack) != 0:
            self.min_val = min(self.stack)
        else:
            self.min_val = sys.maxint

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_val

if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert -3 == minStack.getMin()
    minStack.pop()
    assert 0 == minStack.top()
    assert -2 == minStack.getMin()

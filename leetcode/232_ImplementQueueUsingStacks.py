class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_primary = []
        self.stack_standby = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        # Move primary stack to stand-by stack
        while len(self.stack_primary) != 0:
            peek_val = self.stack_primary[len(self.stack_primary) - 1]
            self.stack_primary.pop()
            self.stack_standby.append(peek_val)

        # Append the element to to be added.
        self.stack_standby.append(x)

        # Move standby stack to primary stack
        while len(self.stack_standby) != 0:
            peek_val = self.stack_standby[len(self.stack_standby) - 1]
            self.stack_standby.pop()
            self.stack_primary.append(peek_val)

    def pop(self):
        """
        :rtype: nothing
        """
        self.stack_primary.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack_primary[len(self.stack_primary) - 1]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack_primary) == 0


if __name__ == '__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)

    while not q.empty():
        print q.peek()
        q.pop()
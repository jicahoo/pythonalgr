# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
At first, I use Queue which is heavy data structure, since it is designed for concurrent scenario. It only beats 6%.
So I tried deque below and the improved solution beat 68% (the best score).
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        import Queue
        q = Queue.Queue()
        q.put(root)
        q.put(None)

        r = [[]]

        while not q.empty():
            node = q.get()
            if node is None:
                if q.empty():
                    break
                q.put(None)
                r.append([])
            else:
                r[len(r)-1].append(node.val)
                left = node.left
                right = node.right
                if left is not None:
                    q.put(left)
                if right is not None:
                    q.put(right)
        return r
'''

'''
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        import collections
        q = collections.deque()
        q.appendleft(root)
        q.appendleft(None)

        r = [[]]

        while len(q) != 0:
            node = q.pop()
            if node is None:
                if len(q) == 0:
                    break
                q.appendleft(None)
                r.append([])
            else:
                r[len(r)-1].append(node.val)
                left = node.left
                right = node.right
                if left is not None:
                    q.appendleft(left)
                if right is not None:
                    q.appendleft(right)
        return r
'''


# Solution that using pre-order traverse. More clear.
class Solution(object):
    def __init__(self):
        self.res = []

    def helper(self, node, depth):
        if node:
            val = node.val
            if len(self.res) <= depth:
                self.res.append([])
            self.res[depth].append(val)
            self.helper(node.left, depth + 1)
            self.helper(node.right, depth + 1)

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        self.helper(root, 0)
        return self.res


if __name__ == '__main__':
    root = TreeNode(3)
    node_9 = TreeNode(9)
    root.left = node_9
    node_15 = TreeNode(15)
    node_7 = TreeNode(7)
    node_20 = TreeNode(20)
    node_20.left = node_15
    node_20.right = node_7
    root.right = node_20

    s = Solution()
    print s.levelOrder(root)
    print s.levelOrder(None)

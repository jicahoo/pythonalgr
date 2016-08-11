class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is not None:
            import Queue
            q = Queue.Queue()
            q.put(root)
            q.put(None)
            s = [[]]
            while not q.empty():
                cur = q.get()
                if cur is None:
                    if q.empty():
                        break
                    s.append([])
                    q.put(None)
                else:
                    s[len(s) - 1].append(cur.val)
                    left = cur.left
                    if left is not None:
                        q.put(left)
                    right = cur.right
                    if right is not None:
                        q.put(right)
            s.reverse()
            return s
        else:
            return []
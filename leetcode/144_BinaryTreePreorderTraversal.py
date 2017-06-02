# Definition for a binary tree node.
import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Beats 78%.
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        stack = []
        if root is not None:
            stack.append(root)
            while len(stack) != 0:
                top_element = stack.pop()
                result.append(top_element.val)
                if top_element.right is not None:
                    stack.append(top_element.right)
                if top_element.left is not None:
                    stack.append(top_element.left)
        return result


class SolutionTest(unittest.TestCase):
    def test_solution(self):
        s = Solution()

        # Case 1: simple tree
        root = TreeNode(1)
        left = TreeNode(2)
        right = TreeNode(3)
        root.left = left
        root.right = right

        self.assertEqual([1,2,3], s.preorderTraversal(root))

        # Case 2: root -> left -> left -> left
        root = TreeNode(-1)
        temp_root = root
        for i in range(5):
            node = TreeNode(i)
            temp_root.left = node
            temp_root = node

        self.assertEqual([-1, 0, 1, 2, 3, 4], s.preorderTraversal(root))

        # Case 3: root - right -> right -> right
        root = TreeNode(-1)
        temp_root = root
        for i in range(5):
            node = TreeNode(i)
            temp_root.right = node
            temp_root = node

        self.assertEqual([-1, 0, 1, 2, 3, 4], s.preorderTraversal(root))

        # Case 4: a normal tree
        '''
                0
               / \
              1   2
             / \   \
            3   4   5
           / \  /   /
          6   7 8   9

        '''
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)
        root.left.left.left = TreeNode(6)
        root.left.left.right = TreeNode(7)
        root.left.right.left = TreeNode(8)
        root.right.right = TreeNode(5)
        root.right.right.left = TreeNode(9)
        self.assertEqual([0, 1, 3, 6, 7, 4, 8, 2, 5, 9], s.preorderTraversal(root))


if __name__ == '__main__':
    unittest.main()

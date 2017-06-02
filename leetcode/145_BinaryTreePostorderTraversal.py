# Definition for a binary tree node.
import unittest


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal_v1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        last_pop = None
        if root is not None:
            last_pop_is_right = False
            while True:
                #First try will infinite loop. Just add last_pop_is_right to avoid goes into the right child tree twice.
                if not last_pop_is_right:
                    while root is not None:
                        stack.append(root)
                        root = root.left

                top_node = stack[-1]
                if top_node.right is None or top_node.right is last_pop:
                    last_pop = stack.pop()
                    result.append(last_pop.val)
                    while len(stack) != 0 and stack[-1].right is None:
                        last_pop = stack.pop()
                        result.append(last_pop.val)

                    if len(stack) == 0:
                        break
                    else:
                        if stack[-1].right is last_pop:
                            last_pop_is_right = True
                        root = stack[-1].right
                else:
                    last_pop_is_right = False
                    root = top_node.right

        return result

    def postorderTraversal_V2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        last_pop = None
        if root is not None:
            while True:
                while root is not None:
                    stack.append(root)
                    root = root.left

                top_node = stack[-1]
                if top_node.right is None or top_node.right is last_pop:
                    last_pop = stack.pop()
                    result.append(last_pop.val)
                    while len(stack) != 0 and (stack[-1].right is None or stack[-1].right is last_pop):
                        last_pop = stack.pop()
                        result.append(last_pop.val)

                    if len(stack) == 0:
                        break
                    else:
                        root = stack[-1].right
                else:
                    root = top_node.right

        return result


    #Beats 3%,3%,78%.
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        last_pop = None
        if root is not None:
            while True:
                while root is not None:
                    stack.append(root)
                    root = root.left

                if len(stack) != 0:
                    if stack[-1].right is None or stack[-1].right is last_pop:
                        last_pop = stack.pop()
                        result.append(last_pop.val)
                    else:
                        root = stack[-1].right
                else:
                    break

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

        self.assertEqual([2, 3, 1], s.postorderTraversal(root))

        # Case 2: root -> left -> left -> left
        root = TreeNode(-1)
        temp_root = root
        for i in range(5):
            node = TreeNode(i)
            temp_root.left = node
            temp_root = node

        self.assertEqual([4, 3, 2, 1, 0, -1], s.postorderTraversal(root))

        # Case 3: root - right -> right -> right
        root = TreeNode(-1)
        temp_root = root
        for i in range(5):
            node = TreeNode(i)
            temp_root.right = node
            temp_root = node

        self.assertEqual([4, 3, 2, 1, 0, -1], s.postorderTraversal(root))

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
        self.assertEqual([6, 7, 3, 8, 4, 1, 9, 5, 2, 0], s.postorderTraversal(root))


if __name__ == '__main__':
    unittest.main()

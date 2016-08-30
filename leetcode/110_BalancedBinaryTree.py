class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.lookup = {}

    def h(self, root_node):
        if root_node in self.lookup:
            return self.lookup[root_node]
        if root_node is None:
            return 0
        height_left = self.h(root_node.left)
        height_right = self.h(root_node.right)
        max_height = max(height_left, height_right)
        height_root = max_height + 1
        self.lookup[root_node] = height_root
        return height_root

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        h_left = self.h(root.left)
        h_right = self.h(root.right)
        is_root_balanced = False
        if abs(h_left - h_right) <= 1:
            is_root_balanced = True
        is_left_balanced = self.isBalanced(root.left)
        is_right_balanced = self.isBalanced(root.right)
        return is_root_balanced and is_left_balanced and is_right_balanced


if __name__ == '__main__':
    root = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_2_dup = TreeNode(2)
    node_3_dup = TreeNode(3)
    node_4_dup = TreeNode(4)
    root.left = node_2
    root.right = node_2_dup
    node_2.left = node_3
    node_2.right = node_4
    node_2_dup.left = node_4_dup
    node_2_dup.right = node_3_dup
    s = Solution()
    print s.isBalanced(root)
    node_5 = TreeNode(5)
    node_3_dup.left = node_5
    node_6 = TreeNode(6)
    node_5.left = node_6
    print s.isBalanced(root)

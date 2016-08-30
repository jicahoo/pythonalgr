# Beat 47%

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        left = root.left
        right = root.right
        if left is None and right is None:
            return True
        elif (left is None and right is not None) or (left is not None and right is None):
            return False
        elif left.val != right.val:
            return False
        else:
            layer = [left, right]
            while len(layer) != 0 and (len(layer)) % 2 == 0:
                n = len(layer)
                mid = n / 2
                for k in xrange(0, mid):
                    i = mid - k - 1
                    j = mid + k
                    left_node = layer[i]
                    right_node = layer[j]
                    is_child_mirror = False

                    if left_node.left is None and right_node.right is None:
                        if left_node.right is None and right_node.left is None:
                            is_child_mirror = True
                        elif (left_node.right is not None and right_node.left is not None) and (
                            left_node.right.val == right_node.left.val):
                            is_child_mirror = True
                        else:
                            is_child_mirror = False
                    elif (left_node.left is not None and right_node.right is not None) and (
                        left_node.left.val == right_node.right.val):
                        if left_node.right is None and right_node.left is None:
                            is_child_mirror = True
                        elif (left_node.right is not None and right_node.left is not None) and (
                            left_node.right.val == right_node.left.val):
                            is_child_mirror = True
                        else:
                            is_child_mirror = False
                    else:
                        is_child_mirror = False
                    if not is_child_mirror:
                        return False
                next_layer = []
                for node in layer:
                    if node.left is not None:
                        next_layer.append(node.left)
                    if node.right is not None:
                        next_layer.append(node.right)
                layer = next_layer
            if len(layer) != 0:
                return False
            return True


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
    print s.isSymmetric(root)

    node_2.left = None
    node_2.right = node_3
    node_3.left = None
    node_3.right = None
    node_2_dup.left = None
    node_2_dup.right = node_3_dup
    node_3_dup.left = None
    node_3_dup.right = None
    print s.isSymmetric(root)

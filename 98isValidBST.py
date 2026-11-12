# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isValidBST(self, root):
        def check(node, low, high):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            return check(node.left, low, node.val) and check(node.right, node.val, high)
        return check(root, float('-inf'), float('inf'))

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if not root:
            return True
        #新数组 ，上升的
        nums = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
            return nums
        inorder(root)
        for i in range(1,len(nums)):
            if nums[i] <= nums[i - 1]:
                return False
        return True

        # 递归中序遍历
       
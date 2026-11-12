# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        def build(l,r):
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = build(l,mid - 1)
            node.right = build(mid + 1,r)
            return node
        return build(0,len(nums) - 1)
#需要开辟新空间，因为数组赋值        
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        #取中间，去递归
        if len(nums) == 0:
            return None
        root = TreeNode()
        # root.left = None
        # root.right = None
        le = len(nums)
        root.val = nums[le//2]
        left = nums[0:le//2]
        right = nums[le//2 + 1:]
        root.left = self.sortedArrayToBST(left)
        root.right = self.sortedArrayToBST(right)
        return root

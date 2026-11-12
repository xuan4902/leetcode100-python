# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        res = []
        cur = root
        while cur or res:
            while cur:
                res.append(cur)
                cur = cur.left
            cur = res.pop()
            k -= 1
            if 0 == k:
                return cur.val
            cur = cur.right

    #需要全部便利，较为占用时空间
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        nums = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)
            return nums
        inorder(root)
        return nums[k - 1]
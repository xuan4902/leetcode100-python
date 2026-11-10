# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        #想了就写下来
        self.max_d = 0
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left) 
            right = dfs(node.right)  
            self.max_d = max(self.max_d,right + left)
            return max(left,right) + 1
        
        dfs(root)
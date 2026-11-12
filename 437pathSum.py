# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.res = 0
        cur_sum = 0
        def dfs(root):
            if not root:
                return 
            cur_sum += root.val
            if cur_sum == targetSum:
                self.res += 1
            dfs(root.left)
            dfs(root.right)
            return self.res
        return dfs(root)
    
        #每个节点，全部计数
        #如果这个节点是==值，那就++
        
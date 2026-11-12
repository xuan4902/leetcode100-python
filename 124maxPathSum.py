# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.res = float('-inf')#全局最大值

        def dfs(node):
            if not root:
                return 0
            #有可能负，所有负的不要，与0
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            #当前节点拐弯的路径，左跟右，跟新全局答案
            cur_path = left + node.val + right
            if cur_path > self.res:
                self.res = cur_path
            #返回，只能选一边，给上层
            return node.val + max(left,right)
        
        dfs(root)
        return self.res
        #返回最大长度
        #最大值用max在倒数第二
        
        root_max = 0
        cur_len = 0
        left = self.maxPathSum(root.left)
        right = self.maxPathSum(root.right)
        cur_len = left + right
        root_max = max(root_max,cur_len)
        return max(left,right)
        

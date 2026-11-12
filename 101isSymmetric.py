#对象函数含有这个self，代表他是归方法的，如果没有这个，就代表他是归函数的也就是用完就可以去掉
# - 定义：`def traver(self, node):` → **必须加 self**
# - 内部递归调用：`self.traver(node.left)` → **必须加 self.**

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(l,r):
            #双空
            if not l and not r:
                return True
            #单空
            if not l or not r:
                return False
            #值相等+左左 vs 右右+左右 vs 右左
            return l.val == r.val and check(l.left,r.right) and check(l.right,r.left)
        #返还
        return check(root,root)
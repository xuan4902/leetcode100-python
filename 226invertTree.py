# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        #只需要改变指针就好，左指向右，右指向左
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
        







        # 👉 它只是改节点里面的数字，**没有修改 left、right 指针**！
        # 二叉树的结构（指针关系）没变，只是 val 被换掉了，不是翻转树。
        def traver(node):
            if not node:
                return
            # - 定义：`def traver(self, node):` → **必须加 self**
            # - 内部递归调用：`self.traver(node.left)` → **必须加 self.**
            traver(node.left)
            self.res.append(node.val)
            traver(node.right)

        def sum_traver(node):
            if not node:
                return
            # - 定义：`def traver(self, node):` → **必须加 self**
            # - 内部递归调用：`self.traver(node.left)` → **必须加 self.**
            sum_traver(node.left)
            node.val = self.res.pop()
            sum_traver(node.right)
        self.res = []
        traver(root)
        sum_traver(root)
        return root
        
            
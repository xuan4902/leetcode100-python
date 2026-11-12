# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        #找到当前节点的左子树最右节点，把当前节点的右子树加到“当前节点的左子树最右节点”上
        cur = root
        while cur:
            if cur.left:
                p = cur.left
                while p.right:
                    p = p.right
                p.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

#此方法就是递归（好理解，先序思路）
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        #先递归推平左右
        self.flatten(root.left)
        self.flatten(root.right)

        #保留原来的右子树
        temp_right = root.right
        #把摊平之后的左子树放到right
        root.right = root.left
        root.left = None
        #找到当前这条右链的最后一个节点
        cur = root
        while cur.right:
            cur = cur.right
        #末尾加上右子树
        cur.right = temp_right

# 迭代（栈，标准先序）按先序顺序逐个取出节点，用 pre 把节点串成一条新链
from collections import deque
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        stack = [root]
        pre = None
        while stack:
            node = stack.pop()
            if pre:
                pre.right = node
                pre.left = None
            pre = node
            #栈：先压右，后压左，保证弹出顺序 跟->左->右
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

#无法通过 错误  #dfs向下递归,无法将右子树插入左节点已经有的右子树的末尾
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        #dfs向下递归,无法将右子树插入左节点已经有的右子树的末尾
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            dfs(node.right)
            if node.left:
                while node.right:
                    node = node.right
                node.left.right = node.right
                node.right = node.left
            return node
        dfs(root)
                
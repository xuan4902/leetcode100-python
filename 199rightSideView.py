# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
#dfs 面试常考
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        def dfs(node,depth): 
            if not node:
                return
            #depth为当前长度，代表第一次访问这层
            if depth == len(res):
                res.append(node.val)
            #先右后左
            dfs(node.right,depth + 1)
            dfs(node.left,depth + 1)
        dfs(root,0)
        return res 
#bfs 广度优先
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        #首root为空
        if not root:
            return []
        #双向链表，好派出队首
        q = deque([root])
        res = []
        #当队列内有值
        while q:
            #判断值（上一层有的，直接保留）
            level_len = len(q)
            #在有的上一层循环
            for i in range(level_len):
                node = q.popleft()
                #如果是这一层最后一个节点，加入res
                if i == level_len - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res


        

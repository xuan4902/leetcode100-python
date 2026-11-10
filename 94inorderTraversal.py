# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        #       1
        #     /   \
        #    2     3
        #   / \
        #  4   5
        # 先1 → 2 → 4 → 5 → 3
        # 中4 → 2 → 5 → 1 → 3
        # 后4 → 5 → 2 → 3 → 1
#前序遍历
    #递归
    def preorder(self,root,res): 
        if not root:
            return
        res.append(root.val)
        self.preorder(root.left,res)
        self.preorder(root.right,res)
    #迭代
    def preorderIter(self,root): 
        if not root :return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if root.right:
                stack.append(node.right)
            if root.left:
                stack.append(node.left)
        return res

    #中序遍历
    def inorder(self,root,res):
        if not root: 
            return 
        self.inorder(root.left,res)
        res.append(root.val)
        self.inorder(root.right,res)
        
    def inorderIter(self,root):
        if not root: return []
        stack = []
        res = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            res.append(root.val)
            root = root.right
        return res

    #后续遍历
    def postorder(self,root,res):#post-order：后序
        if not root: 
            return 
        self.postorder(root.left,res)
        self.postorder(root.right,res)
        res.append(root.val)
   
    def postorderIter(self,root):
        if not root: return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)            
            if node.right:
                stack.append(node.right)
        return res[::-1]
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#    - 带`self.`：**对象全局（该实例下所有方法互通）**
#    - 不带 self，写在 def 第一行：**仅限这个函数自己**
#    - 不带 self，写在函数里面、再套一层 def：**仅限这一组嵌套函数**
class Solution(object):
    #递归
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right) + 1  # + 1 是加下一层
    #回溯+dfs
    def maxDepth(self, root):
        #`self.max_dep`：**实例属性**，属于这个 Solution 对象，嵌套 dfs 内部可以修改、读到这个变量。
        # 不加 self、直接写`max_dep`：**普通局部变量**，作用域只在`maxDepth`函数，嵌套函数dep修改它会触发`UnboundLocalError`。
        self.max_dep = 0
        # - 如果 `dep` 是**写在 class 里面、def 开头的成员方法**：**必须写 self，而且 self 放第一个参数**
        # - 如果 `dep` 是**写在 maxDepth 内部、嵌套定义的函数（像刚才 dfs 那种）：不要加 self**
        dep(root,0)
        def dep(node,cur):
            if not node:
                return
            cur += 1
            if cur > self.max_dep:
                cur_dep += 1
            dep(root.left,cur)
            dep(root.right,cur)
        return self.max_dep

        
# Definition for a binary tree node.

### `map(func, iterable)`
# **作用：把迭代器里每一个元素，批量交给函数处理，返回一个迭代器*  *和哈希表、dict 完全无关！list(map(lambda x:x*2, nums)) 
#  map(lambda x:x*2, nums) = `[x*2 for x in nums]`

# 函数	作用	返回值	核心逻辑
# map(func, seq)	变换 / 映射：每个元素加工一遍	迭代器	func(元素)，一对一转换list(map)
# filter(func, seq)	筛选：保留满足条件的元素	迭代器	func 返回 True 就留下这个元素list(map)
# reduce(func, seq)	聚合 / 归约：不断把两个元素合并成一个	单个值	func(累计结果, 当前元素)，从左往右滚动合并
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        self.hashmap = {val:i for i ,val in enumerate(inorder)}
        def dfs(pre_l,pre_r,in_l,in_r):
            if pre_l > pre_r:
                return None
            root_val = preorder[pre_l]
            root = TreeNode(root_val)
            mid = self.hashmap[root_val]
            left_len = mid - in_l
            root.left = dfs(pre_l + 1,pre_l + left_len,in_l,mid - 1)
            root.right = dfs([pre_l + left_len + 1,pre_r,mid + 1,in_r])
            return root
        return dfs(0,len(preorder) - 1,0,len(inorder)-1)

#递归
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        #递归终止 ：空数组
        if not preorder or not inorder:
            return None
        #先序第一个是跟
        root_val = preorder[0]
        root = TreeNode(root_val)
        #中序中找到跟的位置
        idx = inorder.index(root_val)
        #左子树：先序【1：idx+1】，中序【0：idx】(idx)就是跟，已经归类了
        root.left = self.buildTree(preorder[1:idx + 1],inorder[:idx])
        #右子树：先序【idx+1：】，中序【idx+1：】
        root.right = self.buildTree(preorder[idx + 1:],inorder[idx + 1:])
        return root

        

            
        
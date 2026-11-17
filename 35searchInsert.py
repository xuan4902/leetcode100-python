class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums)
        def dfs(l,r,target):
            if l == r:
                return r          
            elif nums[(l + r)//2] >= target:
                return dfs(l,(l + r)//2,target)
            elif nums[(l + r)//2] < target:
                return dfs((l + r)//2 + 1,r,target)
            
        return dfs(l,r,target)
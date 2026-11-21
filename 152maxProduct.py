class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) 
        ans = curMin = curMax = nums[0] 
        for i in range(1,n):
            #先存旧的curmax
            oldMax = curMax
            curMax = max(nums[i],oldMax * nums[i],curMin * nums[i])
            curMin = min(nums[i],oldMax * nums[i],curMin * nums[i])
            ans = max(curMax,ans)
        return ans
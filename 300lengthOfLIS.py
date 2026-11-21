class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        stack = []
        for i in range(len(nums)):
            while stack and stack[-1] > nums[i]:
                stack.pop()
            if stack[-1] == nums[i]:
                continue
            stack.append(nums[i])
            res = max(res,len(stack))
        return res
            
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                i += 2
            else:
                return nums[i] 
        return nums[i]

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # - a ^ a = 0
        # - a ^ 0 = a
        res = 0
        for x in nums:
            res ^= x
        return res
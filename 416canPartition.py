class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        #变成找与其一半相同的了
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True#和为0，不选任何数

        for num in nums:
            #01背包，从后往前遍历，防止重复选同一个数
            #因为如果从前面向后，会变成重复的n个
            for j in range(target,num - 1,-1):
                dp[j] = dp[j] or dp[j - num]
            if dp[target]:
                return True
        return dp[target]
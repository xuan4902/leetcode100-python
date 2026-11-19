class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return 0
        far = 0
        end = 0
        step = 0
        #遍历到倒数第二个就行，最后一个不用跳
        for i in range(n - 1):
            #动态更新能到的最远距离
            far = max(far,i + nums[i])
            #走到当前这一跳的边界，必须起跳
            if i == end:
                step += 1
                end = far
                #提前剪枝：已经够到达终点 在前一个需要跳的节点提前剪枝
                if end >= n - 1:
                    break
        return step

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1,min(i + nums[i] + 1,n)):
                dp[j] = min(dp[j],dp[i] + 1)
        return dp[-1]
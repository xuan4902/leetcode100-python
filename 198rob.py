class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        path = [0] * n
        path[0] = nums[0]
        path[1] = max(nums[0], nums[1]) # 前两间选大的！这里也是你漏的点
        for i in range(2, n):#他找的是到这个最大的，前一个大也可以选择不要这个
            # 二选一：不抢i=path[i-1]；抢i=path[i-2]+nums[i]
            path[i] = max(path[i-1], path[i-2] + nums[i])
        return path[-1]

#错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误，没有想到取大数
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        path = [0] * len(nums)
        path[0] = nums[0]
        path[1] = nums[1]#错一，应该是max（【0】，【1】）
        for i in range(2,len(nums)):
            #错误2，没考虑前一个大
            path[i] = path[i] + path[i - 2]
            #应该是path【i】 = max（  （i） +  （i-2） ）
            res = max(path[i],path[i - 1])
        return res
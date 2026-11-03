#dp动态规划解法
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur = max_sum = nums[0]
        for i in nums[1:]:#从下标1开始，不然会使其变nums【0】+nums【0】
            #取当前值大的
            cur = max(i,cur + i)
            #取最大的
            max_sum = max(max_sum,cur)
        return max_sum


#前缀和解法
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #初始化为0
        pre_nums = [0]
        for i in range(len(nums)):
            pre_nums.append(pre_nums[-1] + nums[i])
        min_pre = pre_nums[0]
        max_val = float('-inf')
        #前缀和 ：pre[j] - pre[i] i < l
        for j in range(1,len(pre_nums)):
            # 拿最大减去最小，你根本不知道原来最小的那个前缀和，是不是在最大的那个前缀和的左边！
                # 如果是sorted
            #先取最大值，后更新，不然如果单独-5，那就错误，直接取0了
            max_val = max(max_val,pre_nums[j] - min_pre)
            if pre_nums[j] < min_pre:
                min_pre = pre_nums[j]
        return max_val
#前缀积 后缀积
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        right = 1
        left = 1
        #左
        for i in range(n):
            #res[i] = left这里用乘号也可以，只是用称号了时间多花点无益，1*n=n
            res[i] = left
            left *= nums[i]
        #右
        for i in range(n - 1,-1,-1):
            #不用i - 1是因为可以不考虑别界，直接考虑全部
            res[i] *= right
            right *= nums[i]
        return res



#左位移，右位移,法不行，会有0
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 1
        for i in nums:
            sum *= i
            # `i = i <<1` 只是修改循环变量 i，不会改动原数组 nums
            i = i << 1

        sum = sum >> 1

        for i in nums:
            i = i * sum
        return nums

        
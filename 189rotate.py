#三次反转法
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def reverse(l,r):
            #反转nums【】闭区间
            while r > l:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1

        n = len(nums)
        k = k % n
        reverse(0,n)
        reverse(0,k - 1) 
        reverse(k,n - 1)
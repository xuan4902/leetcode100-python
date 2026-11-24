class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #三个指针，少想了一个curr
        p0 = 0
        curr = 0
        p2 = len(nums) - 1
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0],nums[curr] = nums[curr],nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:#nums[curr] == 2:
                nums[curr],nums[p2] = nums[p2],nums[curr]
                p2 -= 1

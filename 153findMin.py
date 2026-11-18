class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        n = len(nums)
        right = n - 1

        def dfs(l,r):
            if l > r:
                return
            if l == r:
                return nums[l]
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                #返回的是mid + 1，因为mid肯定不对
                return dfs(mid + 1,r)
            else:
                return dfs(l,mid)
        #找到左边比较大的
        return dfs(left,right)
        #找到右边比较小的

class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums)-1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

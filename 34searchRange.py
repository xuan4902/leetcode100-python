class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        # 第一步：找最小值下标 pivot（旋转分界点，闭区间 [l,r]）
        def find_pivot(l, r):
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                return find_pivot(mid + 1, r)
            else:
                return find_pivot(l, mid)
        pivot = find_pivot(0, n-1)

        # 普通有序二分，闭区间 [l,r]
        def binary_search(l, r):
            if l > r:
                return -1
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return binary_search(mid + 1, r)
            else:
                return binary_search(l, mid - 1)
        
        # 分区搜索，修复pivot=0（没有旋转）的情况
        if pivot == 0:
            # 数组完全有序，直接全局二分
            return binary_search(0, n-1)
        if target >= nums[0]:
            # 在左边高区 [0, pivot-1]
            return binary_search(0, pivot - 1)
        else:
            # 在右边低区 [pivot, n-1]
            return binary_search(pivot, n - 1)


#错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误错误
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 找左边界：第一个 <= target 的位置
        def find_left(l,r):
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] >= target:
                return find_left(l,mid)
            else:
                return find_left(mid + 1,r)
        # 找右边界：第一个 > target 的位置
        def find_right(l, r):
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] > target:
                return find_right(l, mid)
            else:
                return find_right(mid + 1, r)

        left = find_left(0,len(nums))
        right =find_right(0,len(nums))
        #左右相等就说明不存在target
        if left == right:
            return[-1,-1]
        else:
            return[left,right - 1]

        
#如果全都满足，则直接变成O（n）
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        def dfs(l,r,target):
            if l == r:
                if l >= n or nums[l] != target:
                    return [-1,-1]
                # 找到一个，左右扩散
                while nums[l - 1] == target and l >= 1:
                    l -= 1
                while nums[r + 1] == target and r < n - 1:
                    r += 1
                return [l,r]

            mid = (l + r) // 2
            if nums[mid] < target:
                return dfs(mid + 1,r,target)
            elif nums[mid] >= target:
                return dfs(l,mid,target)
        return  dfs(0,n,target)
        
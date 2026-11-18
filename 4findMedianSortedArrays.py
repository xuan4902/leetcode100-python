class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #确保num1是短数组，减少二分的次数
        if len(nums1) > len(nums2):
            nums1,nums2 = nums2,nums1
        m = len(nums1)
        n = len(nums2)
        left,right = 0,m
        total = m + n
        half = (total + 1)//2

        while left <= right:
            i = (left + right) // 2 #nums1取i个放左边
            j = (half - i)  #nums2取j个放左边

            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            if left1 > right2:
                #nums1左边太大，向左移动
                right = i - 1
            elif left2 > right1:
                #nums1左边太小，向右移动
                left = i + 1
            else:
                #找到合法切割
                if total % 2 == 1:
                    return max(left1,left2)
                else:
                    return (max(left1,left2) + min(right1,right2)) / 2.0
                

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #两个数组比较中位数大小
        #找到小的，归到左边
        #继续找，找到len/2的就直接返还
        m = len(nums1)
        n = len(nums2)

        if (m + n) % 2 == 0:
            return     
        all_le = 0
        def dfs(l1,r1,l2,r2):
            if all_le == (m + n) // 2:
                return 
            mid1 = (l1 + r1) // 2
            mid2 = (l2 + r2) // 2
            if nums1[mid1] < nums2[mid2]:
                dfs(mid1,r1,l2,r2)
                all_le += mid1 
            else:
                dfs(l1,r1,mid2,l2)
                all_le += mid2

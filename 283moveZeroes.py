#修改前面的值，后面直接补充
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #hash()
        #`hash()` 是 Python 内置函数，**不是存数据的容器**（不是列表、集合），
        # 作用：**给一个对象计算出一个整数哈希值**。
        i = 0
        for num in nums:  
            if num != 0:
                nums[i] = num
                i += 1
        while i < len(nums) :
            nums[i] = 0
            i += 1 
        
            

#双下标，一个是指0，一个指非0
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #指非零的下一个要放的位置
        next_num = 0
        #这里使用下标
        for num in range(len(nums)):
            #指向非0的
            if num != 0:
                # 交换
                nums[num],nums[next_num] = nums[next_num],nums[num]
                next_num += 1
        return nums    



class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #sort就在老的，原地排序，改原来的列表，返回 None
        #sorted,生成新的，不碰原来的列表，返回一个全新排好序的列表
        right_index = len(nums) - 1 
        left_index = 0
        new_nums = sorted(nums)
        listt = []
        #修枝去掉不可能的
        if new_nums[0] > 0 or new_nums[right_index] < 0:
            return []
        if len(new_nums) < 3:
            return []
        else:
            #取一个定数，剩下两个左右双指针
            for num in range(0,len(new_nums) - 2):
                #**选了同样的第一个数**，后面不管 l、r 怎么去重，都会再生成一遍一样的三元组。
                if num > 0 and new_nums[num] == new_nums[num-1]:
                    continue
                #右边界
                right_index = len(nums) - 1 
                #左边界要是在num上加，不能自增
                left_index = num + 1
                while right_index >left_index:
                    # 如果相同出
                    if new_nums[right_index] + new_nums[left_index] == -new_nums[num]:
                        #**`[a,b,c]`**：这是**创建一个新的子列表**（对应题目要求的 `[数字,数字,数字]`）
                        listt.append([new_nums[left_index],new_nums[num],new_nums[right_index]])
                        #**选了第一个数**，后面 l、r 去重，
                        while left_index < right_index and new_nums[right_index] == new_nums[right_index-1]:
                            right_index -= 1
                        while left_index < right_index and new_nums[left_index] == new_nums[left_index+1]:
                            left_index += 1
                        #去重完还要缩下一个，因为-2，-1，0，1，2.只会卡在202，找不到101，oom内存越届
                        left_index += 1
                        right_index -= 1
                    #不同就直接指针收缩
                    elif new_nums[right_index] + new_nums[left_index] > -new_nums[num]:
                        right_index -= 1                    
                    else:
                        left_index += 1
        return listt
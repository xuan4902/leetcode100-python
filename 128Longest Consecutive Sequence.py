# class Solution(object):
#     def longestConsecutive(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         sortNums = sorted(nums)
#         conlen = 0
#         for i in range(1, len(sortNums)):
#             if sortNums[i] - sortNums[i-1] == 1:
#                 conlen = conlen+1
#                 returnlen = conlen
#             else :
#                 conlen = 0
#         return returnlen

#nlog（n）排序版本（O (nlogn)
class Solution(object):
    def longestConsecutive(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #考虑边界
        if not nums:
            return 0
        sortNums = sorted(nums)# O(n log n)
        #最低为0
        max_len = 1
        cur_len = 1
        for i in range(1,len(sortNums)):
            #考虑边界
            if sortNums[i] == sortNums[i-1]:
                continue

            elif sortNums[i] - sortNums[i-1] == 1:
                cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
            else:
                cur_len = 1
        return max_len


#排序版本（O (n))利用set集合是通过hash值之间匹配
class Solution2(object):
    def longestConsecutive(self,nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #判断边界条件
        if not nums:
            return 0
        #变成set，hash直接映射O（1）
        nums_set = set(nums)
        cur_len = 0
        max_len = 0

        for num in nums_set:
            #从头向前看，第一个-1肯定不在，完成初始化，也不可能在因为到了第二个进入到后面的while+1去分辨
            if num - 1  not in nums_set:
                cur_len = 1
                cur_num = num
                #进入到后面的while+1去分辨
                while cur_num + 1 in nums_set: 
                    cur_len += 1
                    cur_num += 1
                max_len = max(cur_len,max_len)
        return max_len
        
#尝试的倒叙，思路不是很好，暂停
    # for num in num_set:
    #     cur_num = num
    #     while cur_num - 1 in num_set:
    #         cur_len += 1 
    #         cur_num -= 1   
    #     max_len = max(cur_len,max_len)
    #     num = cur_num
    #     cur_len = 1





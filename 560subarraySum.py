#子串  一开始题设没看对，因为是可以不连续，要连续的
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pre_sum = 0
        count = 0
        #hash——map是key为pre_sum，value为出现次数
        # `defaultdict(int)` 是**字典的升级版**，它的作用：**访问不存在的 key 时，不会报 KeyError，自动给这个 key 初始化为 0**。
        from collections import defaultdict
        hash_map = defaultdict(int)
        hash_map[0] = 1#初始化，意思是当出现pre_sum = k 就可以直接保存
       

        for i in nums:
            pre_sum += i
            if pre_sum - k in hash_map:#key在hash里面
                # count += 1  错误，这样会使连续两个（既是第二个数等于0）少，以为如果0 0 0 有六个，单纯+1，只有仨，不会算00 000这样连续复合的
                count += hash_map[pre_sum - k]
            #存入hash
            hash_map[pre_sum] += 1
        return count

       
        
        
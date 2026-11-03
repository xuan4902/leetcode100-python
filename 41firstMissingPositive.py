#set去排序
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        set_nums = set(nums)
        n = len(set_nums)

        #n+2是因为左开右闭，n+1就是全正连续
        for i in range(1,n + 2):
            if i not in set_nums:
                return i
            
#桶排序+hash
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        #一定要知道 range是左开右闭
        for i in range(n - 1):
            #当有效正整数and 这个位置上的数并不是下标对应数
                    #nums[nums[i] -1] != nums[i] :  若是nums[i] -1 != i  是这个数应该放在***，如果是【1，1】直接死循环
                    # 在 x 的目标位置 `target_idx` 上，**现在放的数不等于 x**
            while 1 <= nums[i] <= n and nums[nums[i] -1] != nums[i] :
                #将这个数直接换到相应的下标哪里
                idx = nums[i] - 1
                nums[i],nums[idx] = nums[idx],nums[i]
        for i in range(n):
            if nums[i] != 1 + i:
                return 1 + i
        return n + 1

                


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #hash
        #for
        hash_nums = hash(nums)   # ❌ 1. 列表不能hash！list是可变类型，直接报错
        for i in range(1 , len(nums)):
            if not hash(i):       # ❌ 2. hash(i) 只是i的哈希值，不是判断i在不在nums里
                return i


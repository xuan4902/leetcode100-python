class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for idx,num in enumerate(nums):
            need = target - num
            if need in hashmap:
                return [hashmap[need],idx]
            hashmap[num] = idx
        return []

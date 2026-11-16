class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        small = []
        index = [False] * len(nums)

    #从一个头开始遍历，大小是1，2，3，不是按照先获得一个大小
        def dfs(start):
            res.append(small[:])
            for j in range(start,len(nums)):
                if not index[j]:
                    small.append(nums[j])
                    index[j] = True
                    dfs(j + 1)
                    small.pop()
                    index[j] = False
        dfs(0)
        return res

#也是按照尽头，选或者不选
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        small = []
        def dfs(start):
            if start == len(nums):
                res.append(small[:])
                return
            #不选当前数
            dfs(start + 1)
            #选当前数
            small.append(nums[start])
            dfs(start + 1)
            small.pop()
        dfs(0)
        return res

    
# 子集按长度分组输出，短的在前；同长度内部顺序无所谓
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        small = []
        n = len(nums)
        used = [False] * n

        # k：当前要选几个数，从0到n
        def dfs(start, k):
            if len(small) == k:
                res.append(small[:])
                return
            # j从start往后选，不回头，避免 [1,2] [2,1]
            for j in range(start, n):
                if not used[j]:
                    used[j] = True
                    small.append(nums[j])
                    dfs(j + 1, k)
                    small.pop()
                    used[j] = False
        # 核心：k从小到大，先收集长度0，再1，再2...
        for k in range(0, n + 1):
            dfs(0, k)
        return res

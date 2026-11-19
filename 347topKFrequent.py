import heapq    
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1

        heap = []
        #遍历

        for num,cnt in freq.items():
            heapq.heappush(heap,(cnt,num))
                # 往堆里压入一个**元组 `(cnt, num)`**
                # - `cnt`：这个数字的出现频次
                # - `num`：数组里的元素
            if len(heap) > k:
                heapq.heappop(heap)
        return [item[1] for item in heap]


        # 创建集合
        # s1 = set()        # 空集合！⚠️ {} 是空字典，不是空集合
        # s2 = {1,2,3,4}
        # s3 = set([1,2,2,3])  # 自动去重 → {1,2,3}

        # 初始化字典
        # d = {}
        # d = dict()
        # d = {1:3, 2:2, 3:1}

        # 创建列表
        # lst = []                # 空列表
        # lst = [1,2,3,4]
        # lst = list(range(5))    # [0,1,2,3,4]

        # 创建元组
        # t1 = ()          # 空元组
        # t2 = (1,2,3)
        # t3 = 1,2,3       # 不加括号也可以，自动打包成元组
        # t4 = (5,)        # ⚠️ 只有一个元素必须加逗号！(5) 只是数字5，不是元组

        # dict
        #❌ 字典取值是[]不是()
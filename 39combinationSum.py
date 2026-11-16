class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #结果
        res = []
        #中途使用
        path = []
         # 优化：先排序，为了后面可以提前剪枝（如果当前和已经大于target，后面的更大，直接跳过）
        candidates.sort()
        #长度
        n = len(candidates)
        #dfs
        def dfs(start,cur_sum):
            #终止条件
            if cur_sum == target:
                res.append(path[:])
                return
            # # 遍历选择
            # for i in range(start_index, len(candidates)):
            #     # 剪枝：如果当前数字加上去已经超过 target 了，后面的数字更大，肯定也超过，直接结束当前循环
            #     if current_sum + candidates[i] > target:
            #         break 
            #截枝
            elif cur_sum >= target:
                return
            #继续遍历，从i不是i——++
            else:
                for i in range(start,n):#start开始，绝不能回找
                    num = candidates[i]
                    path.append(num)
                    dfs(i,cur_sum + num)
                    path.pop()
        dfs(0,0)
        return res


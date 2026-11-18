class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 以当前弹出的柱子作为矩形的高，能往左边扩到【左边第一个比它矮的】，往右边扩到【右边第一个比它矮的】
        res = 0
        heights = [0] + heights + [0]#前后补0，方便边界
        stack = []
        n = len(heights)
        for i in range(n):
            #如果当前高度<栈顶高度，说明找到右比这个小的
            while stack and heights[i] < heights[stack[-1]]:
                #这个（前）高度
                cur_idx = stack.pop()
                cur_h = heights[cur_idx]
                #宽度    stack[-1]是前一个矮的
                w = i - stack[-1] - 1
                res = max(res,cur_h * w) 
            #相对高的递增（下标记录距离）
            stack.append(i)
        return res
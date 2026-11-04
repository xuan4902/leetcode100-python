#开火车
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res

        #规划四个边界
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        #边界内缩
        while top <= bottom and right >= left:
            #左到右
            for i in range(left,right + 1):
                res.append(matrix[top][i])
            top += 1
            #上到下
                            #需要自动加上步幅-1
            for i in range(top,bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            #还需要判断一次，不然容易有当行回退
            if top <= bottom:
            #右到左
                for i in range(right,left - 1,-1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            if right >= left:
            #下到上
                for i in range(bottom,top - 1,-1):
                    res.append(matrix[i][left])
                left += 1
        return res


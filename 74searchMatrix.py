#是下一行最左大于上一行最右，这个方法可以
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #将矩阵缩成一维向量
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid =(left + right) //2
            #二维to一维 行mid//n，列mid%n
            val = matrix[mid//n][mid%n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
                




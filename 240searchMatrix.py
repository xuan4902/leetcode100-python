#从右上角z字形，因为右上是这一行最大，这一列最小
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        r = 0
        c = n - 1
        #从右上角开始
        while r < m and c >= 0:
            val = matrix[r][c]
            if val == target:
                return True
            # 向左移，目前值大于目标
            elif val > target:
                c -= 1
            #向下动，目前值小于目标
            else:
                r += 1
        return False
                


#丢入hash——set（），但是是O（nm）
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        s = set()
        for row in matrix:
            for num in row:
                s.add(num)
        return target in s
        
        
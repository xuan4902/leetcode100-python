#O(m+n)空间利用率
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #思路，全局的去判断，新开m+n内容，去存储0的行列
        m = len(matrix)#几行
        n = len(matrix[0])#几列
        row = [False] * m
        col = [False] * n
        for i in range(m):
            for l in range(n):
                if matrix[i][l] == 0:
                    row[i] = True
                    col[l] = True
        for i in range(m):
            for l in range(n):
                if row[i] or col[l]:
                    matrix[i][l] = 0


#O(常数)空间利用率
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #思路，区域的去判断，不新开内容，用第一行，第一列去判断
        #先记第一行，第一列有没有0，
        #遍历去获取非第一行第一列的0行与列
        #获得了之后去置0此行与列
        #回头看此第一行第一列是否原来标记0，标记置0
        m = len(matrix)#几行
        n = len(matrix[0])#几列
        first_row_zero = False
        first_col_zero = False
        # 检查第一列有没有0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        # 检查第一行有没有0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        #判断后面有没有行与列  
        for i in range(1,m):
            for l in range(1,n):
                if matrix[i][l] == 0:
                    matrix[i][0] = 0
                    matrix[0][l] = 0
        #注意边界是0
        for i in range(1,m):
            for l in range(1,n):
                if matrix[i][0] == 0 or matrix[0][l] == 0:
                    matrix[i][l] = 0

        # 处理第一行
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        # 处理第一列
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

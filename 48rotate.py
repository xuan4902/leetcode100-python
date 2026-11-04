#n*n反转
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for l in range(i,n):
                matrix[i][l],matrix[l][i] = matrix[l][i],matrix[i][l]

            #    `n/2` 在 python3 里得到**浮点数**，`range` 只能接收整数。 
            #   matrix[i][l] ↔ matrix[i][n-1-l]正确的
        # for i in range(n):
        #    for l in range(n/2 + 1,n):
        #         matrix[n - l][l],matrix[l][n - l] = matrix[l][n - l],matrix[i][l]

        for i in range(n):
            left = 0
            right = n - 1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1
        return matrix
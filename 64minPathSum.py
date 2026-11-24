class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)#行数
        n = len(grid[0])#列数
        path = [[0] * n for _ in range(m)]
        path[0][0] = grid[0][0]
        #填充第一行
        for i in range(1,n):
            path[0][i] = path[0][i - 1] + grid[0][i]
        #填充第一列
        for i in range(1,m):
            path[i][0] = path[i - 1][0]+grid[i][0]

        for i in range(1,m):
            for j in range(1,n):
                path[i][j] = min(path[i - 1][j],path[i][j - 1]) + grid[i][j]
        return path[m - 1][n - 1] 

#一维空间
class Solution(object):
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [0]*n
        dp[0] = grid[0][0]
        # 先初始化第一行
        for j in range(1,n):
            dp[j] = dp[j-1] + grid[0][j]
        
        for i in range(1,m):
            # 每行第一个：只能从上边来
            dp[0] = dp[0] + grid[i][0]
            for j in range(1,n):
                # dp[j]旧值=上面；dp[j-1]本行左边
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]

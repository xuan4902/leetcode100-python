import math 
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        本质就是组合数：\(C_{m+n-2}^{m-1}\)
        return math.comb(m+n-2,m-1)
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #dp[i][j]到达i，j的路径数
        dp = [1] * n
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j] + dp[j - 1]
        return dp[-1]
#DP 求重点的上一个与左一个
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #dp[i][j]到达i，j的路径数
        dp = [[1] * n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]

#暴力dfs
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.res = 0
        def dfs(x,r):
            if x >= m or r >= n:
                return
            if x == m -1 and r == n - 1:
                self.res += 1
            dfs(x + 1,r)
            dfs(x,r + 1)
        dfs(0,0)
        return self.res

            

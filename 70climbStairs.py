class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #动态规划
        # a是虚拟化的节点。a是下标0，初始化为1是因为从第二步算，第二步前只能是1+1
        a,b = 1,1
        for _ in range(2,n + 1):
            # 1. 新的 `a` = 原来的 `b`（旧 dp [i-1] 变成下一轮的 dp [i-2]）
            # 2. 新的 `b` = 原来的 `a + 原来的 b`（算出 dp [i]）
            a,b = b,a + b
        return b
#扩写
class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n
        # a=dp[i-2], b=dp[i-1]
        a, b = 1, 2
        for i in range(3, n+1):
            c = a + b
            a = b
            b = c
        return b

#纯粹暴力
class Solution(object):
    def climbStairs(self, n):
        def dfs(site):
            if site == n:
                return 1
            if site > n:
                return 0
            return dfs(site+1) + dfs(site+2)
        return dfs(0)

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.res = 0
        def dfs(site):
            if site > n:
                return
            if site == n:
                self.res += 1
                return 
            dfs(site + 1)
            dfs(site + 2)
        dfs(0)
        return self.res

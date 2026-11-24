class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        # dp数组 (m+1) * (n+1)


        dp = [[0]*(n+1) for _ in range(m+1)]
        
        # 初始化边界
        # 注意：i、j 从 0 开始，`dp[0][j]` 代表 word1 是空串，要插入 j 次；
        #                     `dp[i][0]` 代表 word2 是空串，要删除 i 次
              j→ word2:  ""  r   o   s
            i↓word1: "" [0] [1] [2] [3]
                    h  [1]
                    o  [2]
                    r  [3]
                    s  [4]
                    e  [5]

        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 如果字符不等，三种操作选最小：

                    # - 替换：`dp[i-1][j-1] + 1`
                    # - 删除 word1 字符：`dp[i-1][j] + 1`
                    # - 插入字符（等价于删除 word2）：`dp[i][j-1] + 1`

                    # \(dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1\)
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        return dp[m][n]

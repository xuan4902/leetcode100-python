class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        #for for 找到跨越性的匹配的
        for i in range(1,m + 1):
            for j in range(1,n + 1):
                # 两个字符相等：左上角 + 1；不等：取上面、左边的最大值。
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 
                else:
                    dp[i][j] = max(dp[i - 1][j],dp[i][j - 1])
        return dp[m][n]

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        m = len(text1)
        n = len(text2)
        dp = [0]*(n+1)
        for i in range(1, m+1):
            prev = 0  # 保存dp[i-1][j-1]
            for j in range(1, n+1):
                temp = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = prev + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev = temp
        return dp[n]

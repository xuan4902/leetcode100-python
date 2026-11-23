#关机思路是，用数组对比
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 1
        start = 0
        #倒序遍历左边界i
        for i in range(n - 1,-1 ,-1):
            for j in range(i,n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                    else:
                        #看看她内部是不是回文
                        dp[i][j] = dp[i + 1][j - 1]
                #更新最长记录
                if dp[i][j] and (j - i + 1) > max_len:
                    max_len = j - i + 1
                    start = i
        return s[start:start + max_len]

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(left,right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            #退出时，【left+1,right -1】才是有效回文
            return left + 1, right - 1

        start,end = 0,0
        for i in range(len(s)):
            #奇数中心
            l1,r1 = expand(i,i)
            #偶数中心
            l2,r2 = expand(i,i + 1)
            #选更长的
            if r1 - l1 > end -start:
                start,end = l1,r1
            if r2 - l2 > end - start:
                start,end = l2,r2
        return s[start:end + 1]
    
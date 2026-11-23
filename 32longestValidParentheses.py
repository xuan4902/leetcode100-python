class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        # 初始一个-1，使其1--1 = 2
        stack = [-1]
        if not s:
            return 0
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else: 
                #((会弹出最后一个，保留前一个下标i这样也是可以计算
                stack.pop()
                if not stack:
                    stack.append(s[i])
                else:
                    res = max(res,i - stack[-1])#原来最长，比现在这个节点到上一个卡壳的地方，过这个卡壳就是相当于stack最前
        return res

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        dp = [0] * n
        for i in range(1,n):
            #仅判断可以合并关上的
            if s[i] == ')':
                #可以关上
                if s[i - 1] == '(':
                    #+这个关上的值（关上前连着关上的）
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                #前一个是))
                else:
                    #找前一个“ ）” ）的前
                    pre = i - dp[i - 1] - 1
                    #如果是（
                    if pre >= 0 and s[pre] == '(':
                        #加起来 中间的  现在前面 i-1 这个位置，已经有一段有效括号，长度是 `dp[i-1]`
                        dp[i] = dp[i - 1] + 2
                        if pre - 1 >= 0:
                            #加前面的（（（）））再看 pre 前面还有没有有效括号（`pre-1`），有的话加上 `dp[pre-1]`
                            dp[i] += dp[pre - 1]
                
                res = max(res,dp[i])
        return res
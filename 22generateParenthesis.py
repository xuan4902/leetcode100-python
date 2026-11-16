class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        path = []
        def dfs(left,right):
            if left == n and right == n:
                res.append("".join(path))
                return
            if left < n: #elif满足 `left < n`，执行加左括号，**后面加右括号的分支直接跳过**
                path.append("(")
                dfs(left + 1,right)
                path.pop()
            if right < left:
                path.append(")")
                dfs(left ,right + 1)
                path.pop()
        dfs(0,0)
        return res
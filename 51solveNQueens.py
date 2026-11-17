class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        path = ["."] * n * n
        dirt = [[0,1],[0,-1],[1,0],[-1,0]]
        in_q = 0
        visted = [False] * n * n
        def dfs(l,r):
            if l < 0 or l >= n or r > 0 or r >= n or visted[l][r]:
                return
            if in_q == n:
                res.append(path)
                visted = [False] * n * n
                path = ["."] * n * n
                return
            path[l][r] = "Q"
            for i in range(n):
                visted[l][i] = True
                visted[i][r] = True
                for w in range(n):
                    if w - r // i - l == 1 or w - r // i - l == -1:
                        visted[i][w] = True

            for dx,dy in dirt:
                nl = dx + l
                nr = dy + r
                dfs(nl,nr)
            
        for i in range(n):
            dfs(i,0)
        return res

            
            
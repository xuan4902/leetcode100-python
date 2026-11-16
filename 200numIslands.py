class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #遍历
        #已经访问的下标
        n = len(grid)
        le = len(grid[0])
        #循环调出
        guo = [[False]*n for _ in range(le)]
        res = 0
        
        def dfs(i,j):
            if i < 0 or i >= n   or    j < 0 or j >= le:
                return 
            if grid[i][l] == '0' or guo[i][j]:
                return
            guo[i][j] = True
            dfs(i + 1,l)
            dfs(i ,l+ 1)
            dfs(i - 1,l)
            dfs(i ,l - 1)
        
        for i in range(n):
            for l in range(le):
                if grid[i][l] == '1' and not guo[i][l]:
                    res += 1 
                    dfs(i,l)
                    

                
                dfs()

            

        
from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #m行数，n列数
        m = len(grid)
        n = len(grid[0])
        q = deque()
        fresh = 0
        #方向上下左右
        dirs = [[-1,0],[1,0],[0,-1],[0,1]]

        #统计有多少好的，有多少坏的
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        time = 0
        #多源BFS
        while q and fresh > 0:
            #这一层的数量
            size = len(q)
            for _ in range(size):
                x,y = q.popleft()
                for dx,dy in dirs:
                    nx = x + dx
                    ny = y + dy
                    #在边界内，是新鲜的
                    if 0 <= nx < m and 0 <= ny < n and grid[i][j] == 1:
                        grid[nx][ny] = 2
                        fresh -= 1
                        q.append((nx,ny))
            #扩散完一层，时间+1
            time += 1
        #还有新鲜橘子 -1
        return time if fresh == 0 else -1 


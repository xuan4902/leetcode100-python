from collections import deque
# 方法一：BFS（Kahn 算法 / 入度表法）
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #构建邻接表与入度数组
        adj = [[]for _ in range(numCourses)]
        in_degree = [0] * numCourses#入度

        for cur,pre in prerequisites:#**按子元素内部顺序，依次拆包赋值**，第一个值给 x，第二个给 y
            adj[pre].append(cur) #先学pre才能学cur，边方向pre -》 cur
            in_degree[cur] += 1

        #初始化队列，所有入度为0的课程入队
        q = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        count = 0
        while q:
            node = q.popleft()
            count += 1
            #遍历当前课程的所有所需课程-1（因为是从 所需pre 指向 要学cur ），入度-1
            for next_node in adj[node]:
                in_degree[next_node] -= 1
                if in_degree[next_node] == 0:
                    q.append(next_node)

        return count == numCourses

# 方法二：DFS（深度优先遍历 + 状态标记）
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # 构建邻接表
        adj = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adj[pre].append(cur)
        
        # 0=未访问，1=访问中，2=已访问完成
        visited = [0] * numCourses
        
        def dfs(node):
            if visited[node] == 1:
                return False  # 遇到环
            if visited[node] == 2:
                return True
            
            visited[node] = 1  # 标记为当前路径正在访问
            for next_node in adj[node]:
                if not dfs(next_node):
                    return False
            visited[node] = 2  # 所有后继遍历完成，标记为已访问
            return True
        
        # 遍历每一门课程
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        
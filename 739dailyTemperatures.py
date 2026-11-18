class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n):                
            #当前温度>栈下标对应温度，弹出，记录答案
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx= stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res 
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        tmp = []
        n = len(s)
        def is_palindrome(l,r):
            #判断是不是真回文
            while l <= r:
                if s[l] != s[r]:
                    return False
            l += 1
            r -= 1
            return True

        def backtrack(start):
            #分割到末尾，收集答案
            if start == n:
                res.append(list(tmp))
                return
            #先递归获得单个，后递归获得多个
            #枚举当前起点的所有结束位置
            for end in range(start,n):
                if is_palindrome(start,end):
                    #如果是回文，加入路径
                    tmp.append(s[start:end + 1])
                    #递归，剩下的从end+1 开始分
                    backtrack(end + 1)
                    #撤销选择，回溯
                    tmp.pop()
        backtrack(0)
        return res


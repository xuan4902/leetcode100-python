class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        # 数字映射表
        map_d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        path = []
        n = len(digits)
        def dfs(index):
            #终止条件，当所有数字全部处理完了
            if index == n:
                      # - `""` 是空字符串 → 字符之间**不加任何分隔符**，直接连起来    - 如果写成 `"-".join(path)` 就会拼成 `a-d`，这不是我们想要的
                res.append("".join(path))  #`join` 是字符串方法：**用引号里的内容，把列表里面所有元素拼在一起变成一个字符串**
                return
            #当前数字对应的字母列表
            chars = map_d[digits[index]]
            for c in chars:
                path.append(c)
                dfs(index + 1)
                path.pop()
        dfs(0)
        return res 


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        # 数字映射表
        map_d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        path = []#存放‘a’‘b’这样的字母的
        
        def dfs(index):
            if index == len(digits):
                res.append("".join(path))
                return    
            char = map_d[digits[index]]
            for c in char:
                path.append(c)
                dfs(index + 1)
                path.pop()
        dfs(0)
        return res
            

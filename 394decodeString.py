class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = 0#记录数字
        stack = []
        res = ""#当前正在拼接的字符串
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                #把当前状态压栈，之前的字符，当前数字
                stack.append((res,num))
                res = ""
                num = 0
            elif c == ']':
                #出栈，拿到上一层的字符串和次数
                last_str,k = stack.pop()
                res = last_str + res * k
            else:
                #普通字母，直接加入到当前res
                res += c
        return res

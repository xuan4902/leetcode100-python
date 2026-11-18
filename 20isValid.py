class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        #key右括号，value:对应左括号
        mapping = {')':'(',']':'[','}':'{'}
        for c in s:
            if c in mapping:
                #是右括号
                top = stack.pop() if stack else '#'
                if top != mapping[c]:
                    return False
            else:
                #左括号，入栈
                stack.append(c)
        return len(stack) == 0

    
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #栈，判断
        stack = []
        for c in s:
            if stack:
                if c == '}' and stack[-1] == '{':
                    stack.pop()
                elif c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        if not stack:
            return True
        return False

                
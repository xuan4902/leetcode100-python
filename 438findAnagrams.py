class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        result = []
        len_p = len(p)
        #采用计数的方法，提取出现的和重复的
        count_p = [0] * 26
        count_window = [0] * 26
        #先统计p里面出现的频率 ord是取ascll源码
        for i in p:
            count_p[ord(i) - ord('a')] += 1
        #初始化第一个窗口
        for i in range(len_p):
            count_window[ord(s[i]) - ord('a')] += 1          
        if count_window == count_p:
            result.append(0)
        #滑动窗口出现的频率
        for i in range(len_p,len(s)):
            #新增右侧
            count_window[ord(s[i]) - ord('a')] += 1
            #滑动，滑动丢弃的去掉，新增的加入
            left_char = s[i -len_p]
            count_window[ord(left_char) - ord('a')] -= 1
            if count_window ==count_p:
                result.append(i - len_p + 1)
        return result





#错误
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left = 0
        result = []
        #错误，这是直接赋值了
        window = [len(p)]
        window = []
        new_p = sorted(p)
        #for循环去寻找不同的符合结果内容
        for right in range(0,len(s)):
            #剪枝错误
            #i如果不在p里面，直接在这个数后面开始左
            if s[right] not in p:
                left = right + 1
            window.append(s[right])
            if len(window) == len(p):
                window.sort()
                if window == new_p:
                    result.append(left)
                    left += 1
        return result


#错误，要abc，但是abb在这里也可以通过，需要的是统计窗口中出现的次数（允许p重复）
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        left = 0
        result = []
        #for循环去寻找不同的符合结果内容
        for right in range(0,len(s) - len(p) + 1):
            #i如果不在p里面，直接在这个数后面开始左
            if s[right]  not in p:
                left = right + 1
            elif right - left +1 == len(p):
                result.append(left)
                left += 1
        return result

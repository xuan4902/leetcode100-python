#最小覆盖子串
#这题是没有主思路，想到了这一点，但是思路顺不下来
#双指针+hash计数（字典）+valid

#运用字典，将need，key 为字符，valid 为需要的个数  window窗口的
#遍历need，相应值++
#记录left，start，最小长度，valid是t所有字符的和，++才行
#开始循环。当循环到是need，这个winwod++,
#如果 window == need，则说明vliad+，
    #判断，当window == need后，在去减left，使其变得min
    #边界永远是 window == need
        # 减时还需要去更新start，min——left





from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        #dict  A:1 B:2
        need = defaultdict(int)
        window = defaultdict(int)

        #找到所需要的
        for c in t:
            need[c] += 1

        left = 0
        valid = 0
        #记录最小字串的起始位置，长度
        start = 0
        min_len = float('inf') #正向无穷大

        for i in range(len(s)):
            #取字符
            c = s[i]
            #字符是need（t）内的
            if c in need:
                window[c] += 1
                #满足t所有此字符,valid+1 ,因为valid是多个字符的和证明
                if window[c] == need[c]:
                    valid += 1
        
            #去left向右滑动，使其变成最小字串
            while valid == len(need):
                cur_len = i - left + 1
                #更新最优解
                if cur_len < min_len:
                    min_len = cur_len
                    start = left
                #移除左边界字符
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        #更新不到，就是没有
        if min_len == float('inf'):
            return ""
        return s[start:start+min_len]







        
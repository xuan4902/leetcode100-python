#滑动窗口
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #以字符为key，以下标为value
        char_idnex = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            #找字符，也就是key
            c = s[right]
            #字符出现过，并且出现的位置在left之右（后）（前面的char_idnex[c]不是不看，是看了不满足）
            if c in char_idnex and char_idnex[c] >= left:
                left = char_idnex[c] + 1
            #更新长度
            char_idnex[c] = right
            max_len = max(right - left + 1,max_len)
        return max_len

            
        



#暴力
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #打算采用字典，通过字典的key，判断是否有value
        #有value直接终止，记录最长
        # 没有value，len++
        max_len = 0
        for i in range(len(s)):
            dict = {}
            cur_len = 0
            for l in range(i,len(s)):
                if s[l] in dict:
                    break
                dict[s[l]] = True
                cur_len += 1
                if cur_len > max_len:
                    max_len = cur_len
        return max_len
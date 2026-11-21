class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        word_set = set(wordDict)#把单词列表转为哈希集合，利用集合 O (1) 的查找特性，降低每次判断子串是否在字典里的时间开销。
        n = len(s)
        res = [False] * (n + 1) #长度是n+1，下标从0~n
        res[0] = True
        for i in range(1,n + 1):
            for j in range(i):#不包右，所有就是到前一个
                if res[j] and s[j:i] in word_set:#j 到 i 这一段子串，如果刚好在单词字典里，s[j:i]不包含i
                    res[i] = True#所以直接让i（下一个）当起点的变成true
                    break
        return res[n]
    
                
                    
        
         
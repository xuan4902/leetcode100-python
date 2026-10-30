# 通用滑动窗口模板版本（need/window/valid，背诵万能模板）

# 适合所有滑动窗口：最小覆盖子串、无重复最长子串、这道题都能用
# 思路：维护满足条件的有效匹配数 `valid`，不用每次比较整个数组，效率一样，面试常考
class Solution(object):
    def findAnagrams(self, s, p):
        from collections import defaultdict
        #`defaultdict(int)`：访问不存在的 key 时，**自动默认值是 0**，不会报错。
        need = defaultdict(int)
        window = defaultdict(int)
        for c in p:
            need[c] += 1
        
        left = 0
        valid = 0   #满足频次要求的字符种类数量
        res = []
        k = len(p)

        for right in range(len(s)):
            c = s[right]
            if c in need:
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            
            # 窗口超过固定长度，收缩左边
            while right - left + 1 > k:
                d = s[left]
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                left += 1
            # 全部字符频次匹配成功
            if valid == len(need):
                res.append(left)
        return res

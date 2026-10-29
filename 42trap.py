#接雨水问题

#双指针解法
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l ,r = 0, len(height) -1
        water = 0
        left_max = right_max = 0
        #左右指针相同了，退出
        while l < r:
        #左，右指针比大小，小的自动向中间和
            if height[l] < height[r] :
                if height[l] >= left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l += 1
            else:
                if height[r] >= right_max:
                    right_max = height[r]
                else:
                    water += right_max - height[r]
                r -= 1
        return water
                
        #左指针向右走，如果比他小（平），就说明可以存水
        #左指针向右走，比他大，则换，换了之后在走
        #右指针向左走，如果比他小（平），就说明可以存水
        #右指针向左走，比他大，则换，换了之后在走


#栈的方法
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        water = 0
        for i ,h in enumerate(height):
            while stack and h > height[stack[-1]]:
                bottom = stack.pop()
                #判断栈是否为空，空就代表无法装
                if not stack:
                    break
                w = i - stack[-1] - 1 #宽度，从最右边开始算的，stack【-1】是栈顶，一开始i - stack[-1] - 1 只能是1
                dh= min(h,height[stack[-1]]) - height[bottom] #高度，也是和这个最矮的旁边的比(可能是压栈里的，意味着不是左高墙)，高
                water += w * dh
            stack.append(i)
        return water
        


#递归二分，O（n2），直接超时
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        def dfs(l,r):
            #判断出边
            if l >= r:
                return 0
            max_h = -1
            max_index = l
            for i in range(l ,r + 1):
                if max_h < height[i]:
                    max_h = height[i] 
                    max_index = i
            water = 0
            #左
            left_h = 0
            left_h_index = max_index
            for i in range(l,max_index):
                if height[i] > left_h:
                    left_h = height[i]
                    left_h_index = i
            for i in range(left_h_index + 1,max_index):
                water += left_h - height[i]
            water += dfs(l,left_h_index - 1)
            
            #右
            right_h = 0
            right_h_index = max_index
            for i in range(max_index + 1, r + 1):
                if height[i] > right_h:
                    right_h = height[i]
                    right_h_index = i
            for i in range(max_index + 1,right_h_index):
                water += right_h - height[i]
            water += dfs(right_h_index,r) 

            return water
        return dfs(0,len(height) - 1)


#数组的方法，就是从左找一圈，从右找一圈，最后相同的保留（就是能存水的地方）
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n == 0:
            return 0
        
        pre_max = [0] * n
        suf_max = [0] * n

        # 构建前缀最大值：从左向右
        pre_max[0] = height[0]
        for i in range(1, n):
            # 到i位置为止的最大值 = 前一个前缀最大值 和 当前柱子取大
            pre_max[i] = max(pre_max[i-1], height[i])
        
        # 构建后缀最大值：从右向左
        suf_max[-1] = height[-1]
        for i in range(n-2, -1, -1):
            # i右边的最大值 = i+1位置的后缀最大值 和 当前柱子取大
            suf_max[i] = max(suf_max[i+1], height[i])
        
        res = 0
        for i in range(n):
            # 左右挡板取矮的，减去当前柱子高度，就是i处蓄水
            res += min(pre_max[i], suf_max[i]) - height[i]
        return res


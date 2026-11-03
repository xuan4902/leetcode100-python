#滑动窗口最大值
from collections import deque
class Node:
    def _init_(self,val):
        self.val = val
        self.prev = None
        self.next = None

class MyDeque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        q = deque()
        res = []
        #去循环数组
        for i in range(len(nums)):
            #维护队头最大，如果新加进来的，比原来的大，直接弹出原来小的（因为他永远也最大不了）
            #quq维护下标，这样弹出
            while q and nums[i] >= nums[q[-1]]:#必须验证q存在
                q.pop()#pop全部,尾数比当前数小弹出
            q.append(i)

            #为什么que维护下标的原因，这样可以直接去除，不然得维护第二个
            while q[0] <= i - k:
                q.popleft()

            #记录
            if i >=k -1:
                res.append(nums[q[0]])
        return res

        

###队列
#双数组
#栈
#滑动窗口数字相加
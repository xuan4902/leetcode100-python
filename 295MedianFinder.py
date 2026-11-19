import heapq
# 堆只保证：堆顶是最小元素，其他元素只满足堆性质，整体无序。
# 例：堆列表可能是 `[1,3,2,5,4]`，堆顶是 1，但数组不是升序。
class MedianFinder(object):

    def __init__(self):
        self.left = [] #大根堆
        self.right = []#小根堆
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #左边放的是小的最大的，右边放的是大的最小的，他俩取中
        if not self.left or num <= -self.left[0]:#小的最大比当前这个数大，说明这个数是属于左边小的
            heapq.heappush(self.left,-num)
        else:
            heapq.heappush(self.right,num)
        #平衡两个堆的大小
        if len(self.left) > len(self.right) + 1:
            val = -heapq.heappop(self.left)
            heapq.heappush(self.right,val)
        elif len(self.left) < len(self.right):
            val = heapq.heappop(self.right)
            heapq.heappush(self.left,-val)

    def findMedian(self):
        """
        :rtype: float
        """
        #奇数
        if len(self.left) > len(self.right):
            return -self.left[0]
        #偶数
        else:
            return (-self.left[0] + self.right[0]) / 2.0
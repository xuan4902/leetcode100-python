import heapq #**只实现小根堆！没有原生大根堆**。# 底层就是数组，封装了堆的上浮、下沉操作。
class Solution(object):
        # 堆本质是**完全二叉树**，逻辑上是树，底层用数组存放。分两种：
        # - **小根堆（最小堆）**：父节点 ≤ 子节点，**堆顶永远是堆里最小元素**
        # - **大根堆（最大堆）**：父节点 ≥ 子节点，**堆顶永远是堆里最大元素**
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for x in nums:
            heapq.heappush(heap,x)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]
        #Python 没有原生大根堆，**存负数**

        # ```
        # nums = [3,1,4]
        # h = []
        # for x in nums:
        #     heapq.heappush(h, -x)  # 压负数
        # # 取的时候取负
        # print(-heapq.heappop(h)) # 4


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        return nums[n - k]
            

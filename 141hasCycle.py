# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#循环
#跑，如果循环，前面跑得快一定可以追上后面的，套圈
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #一开始不建议先fast = head。next容易越界
        slow = head
        fast = head
        #循环条件
        while fast and fast.next:  #`slow != fast` 对比的是**对象地址（身份）**
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        
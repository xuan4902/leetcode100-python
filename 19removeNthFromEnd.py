# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#快慢指针是最简
# 1. 先让 fast 从 dummy 出发，往前走 n 步
# 2. 之后 fast、slow 同速一步一步走
# 3. fast 走到末尾（`fast.next == None`）停下
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        # **有可能删除头结点**，优先上 dummy！
        dummy.next = head
        slow = dummy
        fast = dummy
        while n != 0:
            fast = fast.next
            n -= 1

        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next

        
        


        
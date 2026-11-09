# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        cur = head
        #k个节点是否还存在
        for _ in range(k):
            if not cur:
                return head
            cur = cur.next
        
        #写一个反转
        cur = head
        pre = None
        for _ in range(k):
            nxt = cur.next
            cur.next = pre 
            pre = cur
            cur = nxt
        #head为这组的尾巴，按下一组递归
        head.next = self.reverseKGroup(cur,k)
        return pre
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 空间 O (1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pA = headA
        pB = headB
        #A+B，相同距离相同节点值
        while pA != pB:
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        return pA

#hash，set值去做  空间 O (m)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        s = set()
        cur = headA
        while cur:
            s.add(cur)
            cur = cur.next
        cur = headB
        while cur:
            if cur in s:
                return cur
            cur = cur.next
        return None


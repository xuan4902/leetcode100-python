            #3推 先把nxt推向远处
            # nxt = cur.next
            # #转 反转链表
            # cur.next = pre
            # #占 从后往前占
            # pre = cur
            # cur = nxt
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        #先反转链表
        def reverse(node):
            pre = None
            cur = node
            while cur:
                nxt = cur.next
                #转 反转链表
                cur.next = pre
                #占 从后往前占
                pre = cur
                cur = nxt
            return pre #因为最后一个就是Node。cur已经变成next了
        #快慢指针找中间点
        slow,fast = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow是后端的起点，反转后半段
        second = reverse(slow)
        p1,p2 = head ,second
        res = True
        while res and p2:#`p2` 这个条件本质是**保护，防止取 None.val**。链表节点为空的时候，不能访问 `.val` 属性。
            if p1.val != p2.val:
                res = False
            p1 = p1.next
            p2 = p2.next
        #这里可以选择将原来的链表反转
        return res
            
#双指针 一个指针指向前（右），一个指针指向当点地

#迭代代码（标准）循环，用循环重复执行同一段逻辑，靠变量不断更新，一步步算出结果。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        pre = None
        cur = head
        while cur:
            next = cur.next#先存后面节点，防止断链
            cur.next = pre#当前节点反向
            pre = cur#保留当前值，pre向前走
            cur = next#保留当前值的原下一个，cur向前走
        return pre#最后pre已经是头节点 

#递归
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #出循环边界，1给的本来就是空或只有1个，，确实到最后一个了
        if not head or not head.next:
            return head
        #12345
        #到最后一个循环回，给赋值5
        #弹出new_head = 5 这事head = 4
        new_head = self.reverseList(head.next)
        #4.next = 5  4.next.next = 4（相当于在5后面接4）
        head.next.next = head
        #断开4.next = 5这一个，防止循环  
                #    不断开环形链表：3 ↔ 4 ↔ 5，这个head的next就不一定是+1，而有可能是-1
                #                    ┌──────────────────────────┐
                #                    ↓                          │
                #                    1 → 2 → 3 → 4 → 5
                #                    └──────────────────────────┘
                # #
        head.next = None
        #进入head = 3 
        #此时head.next = 4,
        #head.next.next = none
        # head.next.next = head  从新赋值 new_head 5，4，3
        #断开连接
        # 以此循环
        return new_head
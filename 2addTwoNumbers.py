# Definition for singly-linked list.

#
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        cur = dummy
        carry = 0#上位数

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            s = v1 + v2 + carry
            carry = s // 10
            cur.next = ListNode(s % 10)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
#长用例超时 / 校验失败
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #栈 先进后出
        l1_stack = []
        l2_stack = []
        all_stack = ListNode()
        #all_stack一开始是空的，你next也就是错误
        cur = all_stack
        while l1:
            l1_stack.append(l1.val)
            l1 = l1.next
        while l2:
            l2_stack.append(l2.val)
            l2 = l2.next

        sum_l1 = 0
        sum_l2 = 0
        while l1_stack:
            sum_l1 = sum_l1 * 10 + l1_stack.pop()
        while l2_stack:
            sum_l2 = sum_l2 * 10 + l2_stack.pop()
        sum = sum_l1 + sum_l2
        #`all_stack` 是已经实例化好的 ListNode 对象，**不是类**！不能加括号调用，应该写成：ListNode（0）
        if sum == 0:
            return ListNode(0)
        while sum > 0:
            node = ListNode(sum % 10)
            cur.next = node
            sum = sum // 10
            cur = cur.next
        return all_stack.next
            

        
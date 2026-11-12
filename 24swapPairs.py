# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #双指针
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            #交换前后
            a.next = b.next
            b.next = a
            pre.next = b

            pre = a#这一组的最后一个，是下一组的开头，要连接上
        return dummy.next


class Solution(object):
    # 1. low 一开始是 dummy，第一轮直接 `low = low.next` → low 跑到第一个节点，**dummy 断联了，没法接上交换后的头**
    # 2. 交换完之后，你没有**保存前驱节点**，下一轮找不到上一组的尾巴，链表会断裂
    # 3. 循环条件顺序写反了，应该先判断 `low.next` 再 `low.next.next`
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #双指针
        dummy = ListNode()
        dummy.next = head
        low = dummy
        fast = dummy
        while low.next and low.next.next:
            low = low.next
            fast = low.next
            fast.next = low
            #交换前后
            low.next = fast.next
            fast.next = low
        return dummy.next


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #归并排序：递归终点，空，单个，本身有序
        if not head or not head.next:
            return head

        #快慢指针找中点，slow是中间前一个
        # `slow, fast = head, head` 这种写法，循环结束后，**slow 落在中间节点（奇数长度）或者后半个起点（偶数）**
        # slow,fast = head,head   
        # 这样可以精准的落在中间的值前一个             
        slow,fast = head,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None #切断

        left = self.sortList(head)
        right = self.sortList(mid)
        #合并；两个有序链表
        return self.merge(left,right)

    def merge(self,left,right):
        dummy = ListNode()
        cur = dummy
        
        while left and right:
            if left.val >= right.val:
                cur.next = right
                right = right.next
            else:
                cur.next = left
                left = left.next
            cur = cur.next
        cur.next = right if right else left
        return dummy.next

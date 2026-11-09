# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        while len(lists) > 1:
            new_list = []
            i = 0
            #两列合并，从头开始
            while i < len(lists):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged = self.merge(l1,l2)
                new_list.append(merged)  
                i += 2
            lists = new_list
        return lists[0] 
#一定要加self
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
#递归分治，中间分开
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        l = self.mergeKLists(lists[:mid])
        r = self.mergeKLists(lists[mid:])
        return self.merge(l, r)
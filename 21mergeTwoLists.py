#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. 链表节点没有 `.top` 属性，入参 `list1`、`list2` 本身就是头节点
# 2. 不能往列表 `listt` 里 append 节点，题目要求**返回链表头节点**，不是 Python 数组
# 3. 比较要拿 `.val`：`head1.val >= head2.val`，不能直接比较节点对象
# 4. 推荐用**虚拟哑节点 (dummy)**，这是链表合并的标准写法

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        #哑节点，方便处理头节点
        dummy = ListNode()
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        #剩下没走完的直接接上去 
        cur.next = list1 if list1 else list2
        # 此时dummy还是哑节点
        return dummy.next
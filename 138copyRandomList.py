"""
# Definition for a Node.

"""
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        #集合，字典,用字典集合去装新的
        #还一个方法是在原节点后面加上新的，到时候新的指向。next就好
        mapping = {}
        cur = head

        #第一轮，只创建新节点，建立映射关系
        while cur:
            mapping[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        #第二轮，给新节点加上next和random指针
        while cur:
            map[cur].next = mapping.get(cur.next)
            map[cur].random = mapping.get(cur.random)
            cur = cur.next

        return mapping.get(head)
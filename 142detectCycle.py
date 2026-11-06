# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#用两次龟兔赛跑
#第一次判断有没有循环
#第二次从全头，和环内一点，还会有相遇，同速度
        #slow 走到相遇点，一共走的路程： 

        # \(S_{slow}=a+b\)

        # fast 速度是 slow 两倍，走的总路程：

        # \(S_{fast}=2(a+b)\)

        # fast 在 slow 进入环之后，会在环里面多绕k整圈（\(k\ge1\)，正整数）才追上 slow。
        # 所以 fast 的路程也可以写成：

        # \(S_{fast}=a+b + k\cdot L = a+b + k(b+c)\)

        # 两个式子联立：

        # \(2(a+b) = a+b + k(b+c)\)

        #\(\boldsymbol{a = c + (k-1)\cdot L}\)

        # ---

        # ### 翻译这个式子是什么意思

        # L 是环的周长，走 L 步等于在环上原地绕一圈，回到原来位置。
        # \((k-1)\cdot L\) 就是在环上随便绕 \((k-1)\) 整圈，**不改变最终停留位置**。
class Solution(object):
    def detectCycle(self, head):
        slow = head
        fast = head
        has_cycle = False
        # 第一步：快慢指针找相遇点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True
                break
        if not has_cycle:
            return None
        # 第二步：一个从头、一个从相遇点，同速走，相遇就是环入口
        p1 = head
        p2 = slow
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1

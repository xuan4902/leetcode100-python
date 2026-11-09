class DLinkedNode:
    def __init__(self,key = 0 ,value = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        #初始化set
        self.capacity = capacity
        self.cache = dict()
        #模拟头尾哨兵
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #获取，hash
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value       

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            new_node = DLinkedNode(key,value)
            self.cache[key] = new_node
            self.add_to_head(new_node)
            self.size += 1
            #超容量了
            if self.size > self.capacity:
                removed = self.remove_tail()
                del self.cache[removed.key]
                self.size -= 1

    def add_to_head(self,node):
        #插入到head后面
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove_node(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_head(self,node):
        self.remove_node(node)
        self.add_to_head(node)

    def remove_tail(self):
        #删除tail前一个节点，返回被删节点
        node = self.tail.prev
        self.remove_node(node)
        return node

        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
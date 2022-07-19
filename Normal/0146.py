"""
请你设计并实现一个满足  LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 10000
0 <= value <= 105
最多调用 2 * 105 次 get 和 put

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List, Dict


class DLinkedNode:
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache: Dict[int, DLinkedNode] = {}

    def get(self, key: int) -> int:
        print("get: {}".format(key))
        if key in self.cache.keys():
            node = self.cache[key]
            self.move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        print("put: {}, {}".format(key, value))
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = DLinkedNode(key, value)
            self.cache.update({key: node})
            self.add_to_head(node)
            self.size += 1
        if self.size > self.capacity:
            del self.cache[self.tail.prev.key]
            self.remove_tail()
            self.size -= 1

    def add_to_head(self, node: DLinkedNode):
        print("add to head {}".format(node.key))
        next: DLinkedNode = self.head.next
        self.head.next = node
        node.next = next
        next.prev = node
        node.prev = self.head

    def remove_node(self, node: DLinkedNode):
        print("remove node {}".format(node.key))
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def remove_tail(self):
        print("remove tail")
        self.remove_node(self.tail.prev)

    def move_to_head(self, node: DLinkedNode):
        print("move to head {}".format(node.key))
        self.remove_node(node)
        self.add_to_head(node)


class LRUController:
    def __init__(self, capacity: int = 10):
        self.cache = LRUCache(capacity)

    def do(self, order: List[str], data: List[List[int]]):
        result = []
        for i in range(len(order)):
            if order[i] == "LRUCache":
                self.cache = LRUCache(data[i][0])
                result.append(None)
            elif order[i] == "put":
                self.cache.put(data[i][0], data[i][1])
                result.append(None)
            elif order[i] == "get":
                ret = self.cache.get(data[i][0])
                result.append(ret)
        return result


if __name__ == '__main__':
    c = LRUController()
    result = c.do(["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
                  [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]])
    print(result)
    result = c.do(["LRUCache", "put", "put", "put", "put", "get", "get"],
                  [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]])
    print(result)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

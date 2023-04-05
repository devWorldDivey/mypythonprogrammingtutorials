""" https://leetcode.com/problems/design-circular-queue/
    622. Design Circular Queue
Input
["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
Output
[null, true, true, true, false, 3, true, true, true, 4]

Explanation
MyCircularQueue myCircularQueue = new MyCircularQueue(3);
myCircularQueue.enQueue(1); // return True
myCircularQueue.enQueue(2); // return True
myCircularQueue.enQueue(3); // return True
myCircularQueue.enQueue(4); // return False
myCircularQueue.Rear();     // return 3
myCircularQueue.isFull();   // return True
myCircularQueue.deQueue();  // return True
myCircularQueue.enQueue(4); // return True
myCircularQueue.Rear();     // return 4
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class MyCircularQueue:

    def __init__(self, k: int):
        self.sizeofqueue = k
        self.lengthofqueue = 0

    def enQueue(self, value: int) -> bool:
        if self.sizeofqueue == self.lengthofqueue:
            return False
        new_node = Node(value)
        if self.lengthofqueue == 0:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.lengthofqueue += 1

        return True

    def deQueue(self) -> bool:
        if self.lengthofqueue == 0:
            return False
        temp = self.front
        if self.lengthofqueue == 1:
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
            temp.next = None

        self.lengthofqueue -= 1

        return True

    def Front(self) -> int:
        if self.lengthofqueue != 0:
            return self.front.value
        else:
            return -1

    def Rear(self) -> int:
        if self.lengthofqueue != 0:
            return self.rear.value
        else:
            return -1

    def isEmpty(self) -> bool:
        if self.lengthofqueue == 0:
            return True

    def isFull(self) -> bool:
        if self.lengthofqueue == self.sizeofqueue:
            return True

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
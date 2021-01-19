class MyCircularDeque:

    def __init__(self, k: int):
        self.q = [None] * (k+1)
        self.max = k+1
        self.front = 0
        self.rear = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.q[self.front] = value
            self.front = (self.front - 1 + self.max) % self.max
            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            self.rear = (self.rear + 1) % self.max
            self.q[self.rear] = value
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[(self.front + 1) % self.max] = None
            self.front = (self.front + 1) % self.max
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.q[self.rear] = None
            self.rear = (self.rear - 1 + self.max) % self.max
            return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[(self.front + 1) % self.max]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        else:
            return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return self.front == (self.rear + 1) % self.max


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

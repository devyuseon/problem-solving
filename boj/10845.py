import sys
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
        self.queue_size = 0
    
    def push(self, x: int):
        self.queue.append(x)
        self.queue_size += 1
    
    def pop(self):
        if self.queue_size == 0:
            return -1
        tmp = self.queue[0]
        del self.queue[0]
        self.queue_size -= 1
        return tmp
    
    def size(self):
        return self.queue_size
    
    def empty(self):
        if self.queue_size == 0:
            return 1
        else:
            return 0
    
    def front(self):
        if self.queue_size == 0:
            return -1
        return self.queue[0]
    
    def back(self):
        if self.queue_size == 0:
            return -1
        return self.queue[self.queue_size-1]

s = Queue()

N = int(input())
for _ in range(N):
    command = sys.stdin.readline().split()
    if len(command) > 1:
        if command[0] == "push":
            tmp = int(command[1])
            s.push(tmp)
    else:
        if command[0] == "pop":
            print(s.pop())
        elif command[0] == "size":
            print(s.size())
        elif command[0] == "empty":
            print(s.empty())
        elif command[0] == "front":
            print(s.front())
        elif command[0] == "back":
            print(s.back())
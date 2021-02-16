import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.stack_top = -1
    
    def push(self, x: int):
        self.stack.append(x)
        self.stack_top += 1
    
    def pop(self):
        if self.stack_top == -1:
            return -1
        tmp = self.stack[self.stack_top]
        del self.stack[self.stack_top]
        self.stack_top -= 1
        return tmp
    
    def size(self):
        return self.stack_top + 1
    
    def empty(self):
        if self.stack_top == -1:
            return 1
        else:
            return 0
    
    def top(self):
        if self.stack_top == -1:
            return -1
        return self.stack[self.stack_top]

s = Stack()

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
        elif command[0] == "top":
            print(s.top())
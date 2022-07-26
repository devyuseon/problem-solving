# pypy3 2043420kb / 4868ms

import sys
input = sys.stdin.readline

class Trie:
    head = {}
    
    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True
        
    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        if '*' not in cur:
            return False
        else: return True

n, m = map(int, input().split())
trie = Trie()

for _ in range(n):
    trie.add(input())
    
cnt = 0
for _ in range(m):
    if trie.search(input()):
        cnt += 1
        
print(cnt)
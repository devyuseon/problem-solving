# 5252. [파이썬 S/W 문제해결 최적화] 1일차 - 공통 단어 검색

import sys
from collections import defaultdict
sys.stdin = open("SWEA\input.txt", "r")

class Trie:
    head = {}
    
    def add(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['*'] = True # 문자열 종료 표시

    def search(self, word):
        cur = self.head
        for ch in word:
            if ch not in cur:
                return False # 한글자라도 없으면 없는것
            cur = cur[ch]
        if '*' in cur:
            return True
        else:
            return False

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    a = [input().strip() for _ in range(n)]
    b = [input().strip() for _ in range(m)]
    words = defaultdict(int)
    
    trie_a = Trie()
    trie_b = Trie()
    for word in a:
        trie_a.add(word) # 사전 등록
        if trie_b.search(word): # 검색
            words[word] += 1
    for word in b:
        trie_b.add(word)
        if trie_a.search(word):
            words[word] += 1
            
    cnt = 0
    for v in words.values():
        if v == 2: cnt += 1
    
    print(f'#{test_case} {cnt}')
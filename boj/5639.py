import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

# 클래스 풀이-> 350328kb / 1148ms
# class Tree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
    
#     def insert(self, value):
#         if value < self.value: # 작을 경우 왼쪽
#             if self.left == None: # 왼쪽 자식노드가 비어있으면 왼쪽 자식 노드로
#                 self.left = Tree(value)
#             else: # 이미 있다면 왼쪽 자식 노드에 대해 insert
#                 self.left.insert(value)
#         else:
#             if self.right == None:
#                 self.right = Tree(value)
#             else:
#                 self.right.insert(value)
    
#     def postorder(self):
#         if self.left != None: # 왼쪽 자식 노드가 존재하지 않을때까지 계속 왼쪽으로
#             self.left.postorder()
#         if self.right != None:
#             self.right.postorder()
#         print(self.value)
        
# pre = []
# while True:
#     try:
#         pre.append(int(input()))
#     except:
#         break

# tree = Tree(pre[0]) # 루트 노드 기준 객체 생성

# for i in range(1, len(pre)):
#     tree.insert(pre[i])

# tree.postorder()

# 배열(재귀) 풀이 -> 637340kb / 680ms

def postorder(nums):
    if len(nums) == 0: # 배열이 비어 있다면 그대로 종료
        return
    
    if len(nums) == 1: # 배열에 값이 하나 있다면 값 출력한 후 종료
        print(nums[0])
        return
    
    idx = len(nums) # 부모 노드 기준으로 값이 커지는 순간의 인덱스
                    # 부모 노드 기준 오른쪽 자식의 인덱스
    for i in range(1, len(nums)):
        if nums[i] > nums[0]:
            idx = i
            break
        
    if idx > 1: # 왼쪽 자식 노드에 대해 재귀 호출
        postorder(nums[1:idx])
    
    if idx < len(nums): # 오른쪽 자식 노드에 대해 재귀 호출
        postorder(nums[idx:])
        
    print(nums[0])  

pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break
postorder(pre)
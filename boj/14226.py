s = int(input())

def dfs(cur, clipboard, time):
    if cur == s:
        return time
    if cur > s:
        # 지운다
        dfs(cur - 1, clipboard, time + 1)
    if cur < s:
        if cur + clipboard < s:
            # 이모티콘 복사해 클립보드에 저장
            dfs(cur, cur, time + 1)
        # 클립보드의 이모티콘 화면에 붙여넣기
        dfs(cur + clipboard, clipboard, time + 1)
        
print(dfs(1, 0, 0))
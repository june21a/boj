import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
score_map = []
for i in range(N):
    score_map.append(list(map(int, input().split())))
visited = [[False for i in range(M)] for j in range(N)]

def check_idx(y, x):
    return y >= 0 and y < N and x >= 0 and x < M and not visited[y][x]


# without T block
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

def dfs(y, x, S, depth):
    if depth == 4:
        global ans
        ans = max(ans, S+score_map[y][x])
        return
    
    visited[y][x] = True
    for i in range(4):
        next_y, next_x = y+dy[i], x+dx[i]
        if check_idx(next_y, next_x):
            dfs(next_y, next_x, S+score_map[y][x], depth+1)

    visited[y][x] = False
    
for i in range(N):
    for j in range(M):
        dfs(i, j, 0, 1)

# for T block
for i in range(N):
    for j in range(M):
        lst = []
        
        for k in range(4):
            next_y, next_x = i+dy[k], j+dx[k]
            if check_idx(next_y, next_x):
                lst.append(score_map[next_y][next_x])
            else:
                lst.append(0)
        ans = max(ans, score_map[i][j] + sum(lst) - min(lst))
print(ans)   
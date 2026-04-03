import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
blue, red = None, None

for i in range(N):
    s = input().strip()
    board.append([c for c in s])

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            blue = (i, j)
        if board[i][j] == 'R':
            red = (i, j)


visited = [
    [[[False for _ in range(M)] for _ in range(N)] for _ in range(M)] for _ in range(N)
]
visited[blue[0]][blue[1]][red[0]][red[1]] = True
q = deque([(*red, *blue, 0)])

move = [
    (0,1), (1,0), (0,-1), (-1,0)
]

ans = -1
while q:
    ry, rx, by, bx, cnt = q.popleft()
    
    if cnt >= 10 or ans != -1:
        break
    
    for dy, dx in move:
        next_ry, next_rx, next_by, next_bx = ry, rx, by, bx
        red_goal, blue_goal = False, False
        
        # red ball move
        while True:
            next_ry, next_rx = next_ry+dy, next_rx+dx
            next_c = board[next_ry][next_rx]

            if next_c == '#':
                next_ry, next_rx = next_ry-dy, next_rx-dx
                break
            elif next_c == 'O':
                red_goal = True
                next_ry, next_rx = -1, -1
                break
            elif next_ry==next_by and next_rx == next_bx:
                next_by, next_bx = next_by+dy, next_bx+dx
                b_next_c = board[next_by][next_bx]
                
                if b_next_c == '#':
                    next_ry, next_rx = next_ry-dy, next_rx-dx
                    next_by, next_bx = next_by-dy, next_bx-dx
                    break
                elif b_next_c == 'O':
                    blue_goal = True
                    break
                else:
                    pass
            else:
                pass
        
        # blue ball move
        while True:
            next_by, next_bx = next_by+dy, next_bx+dx
            next_c = board[next_by][next_bx]

            if next_c == '#' or (next_ry==next_by and next_rx == next_bx):
                next_by, next_bx = next_by-dy, next_bx-dx
                break
            elif next_c == 'O':
                blue_goal = True
                break
            else:
                pass
        
        if red_goal and not blue_goal:
            ans = cnt+1
            break
        
        # check
        if visited[next_ry][next_rx][next_by][next_bx] or blue_goal:
            continue
        q.append((next_ry, next_rx, next_by, next_bx, cnt+1))
        visited[next_ry][next_rx][next_by][next_bx] = True

print(ans)
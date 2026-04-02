import sys
from collections import deque
input = sys.stdin.readline

def get_dir(cur_dir, command):
    num = -1 if command == 'L' else 1
    return (cur_dir + num) % 4
    

N = int(input())
K = int(input())
board = [[0 for _ in range(N)] for _ in range(N)]
for i in range(K):
    y, x = map(int, input().split())
    board[y-1][x-1] = 1 # apple


head = (0, 0)
board[0][0] = 2
move_tracker_q = deque([(0, 0)])

move = {
    0: (0, 1), #right
    1: (1, 0), #down
    2: (0, -1), #left
    3: (-1, 0) #up
}

L = int(input())
trajs = []
for i in range(L):
    a, b = input().split()
    trajs.append((int(a), b))

cnt = 0
cur_dir = 0
cur_traj = 0
while True:
    # direction change
    if cur_traj < L:
        traj_cnt, command = trajs[cur_traj]
        
        if cnt == traj_cnt:
            cur_dir = get_dir(cur_dir, command)
            cur_traj += 1
    
    # head move
    y, x = head
    dy, dx = move[cur_dir]
    next_y, next_x = y+dy, x+dx
    head = (next_y, next_x)
    move_tracker_q.append((next_y, next_x))
    
    # time check
    cnt += 1
    
    # collision check
    if next_y < 0 or next_y >= N or next_x < 0 or next_x >= N or board[next_y][next_x] == 2:
        break
    
    # apple check
    if board[next_y][next_x] == 1:
        pass
    else:
        t_y, t_x = move_tracker_q.popleft()
        board[t_y][t_x] = 0
    board[next_y][next_x] = 2

print(cnt)
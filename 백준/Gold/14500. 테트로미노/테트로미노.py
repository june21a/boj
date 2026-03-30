import sys
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
score_map = []
for i in range(N):
    score_map.append(list(map(int, input().split())))

def check_idx(y, x):
    return y >= 0 and y < N and x >= 0 and x < M

def reverse_xy(block):
    for i in range(4):
        block[i] = block[i][::-1]
    return block

def reverse_x_sign(block):
    for i in range(4):
        block[i][1] *= -1 
    return block

def reverse_y_sign(block):
    for i in range(4):
        block[i][0] *= -1 
    return block

def get_block_by_number(block, number):
    if number & 1:
        block = reverse_xy(block)
    
    if number & 2:
        block = reverse_x_sign(block)
    
    if number & 4:
        block = reverse_y_sign(block)
    return block

# block making
blocks = [
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[0, 0], [0, 1], [1, 1], [0, 2]]
]
additional_block = []
for block in blocks:
    for i in range(1, 8):
        additional_block.append(get_block_by_number(copy.deepcopy(block), i))
blocks.extend(additional_block)

ans = 0
for i in range(N):
    for j in range(M):
        for block in blocks:
            S = 0
            poses = [[i+dy, j+dx] for dy, dx in block]
            
            for (y, x) in poses:
                if check_idx(y, x):
                    S += score_map[y][x]

            ans = max(ans, S)
print(ans)
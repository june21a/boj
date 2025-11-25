import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().split()))
lst = sorted([[num, i+1] for i, num in enumerate(lst)])
q = deque(lst)

ans = []
current = [
    [0, 0], [0, 0]
]

while q:
    if current[0][0] == 0:
        current[0] = q.pop()
    else:
        current[1] = q.pop()
    
    cnt1, num1 = current[0]
    cnt2, num2 = current[1]
    m = min(cnt1, cnt2)
    ans += [num1, num2] * m
    current[0][0] -= m
    current[1][0] -= m

if current[0][0] > 1 or current[1][0] > 1:
    print(-1)
else:
    ans += [current[0][1]]*current[0][0] + [current[1][1]]*current[1][0]
    print(*ans)
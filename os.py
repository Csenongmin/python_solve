import sys
import heapq
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
T = int(input().strip())
for _ in range(T):
    m, n, k = map(int, input().split())
    bae = [set(map(int, input().split())) for _ in range(k)]
    graph = [[0]*m for _ in range(n)]
    q = []
    heapq.heappush([0,0])
    while q:
        x,y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        if 0<= nx < m and 0<= ny < n:
            if (nx, ny) in bae:
                heapq.heappush([nx, ny])
    
    
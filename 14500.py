import sys
input = sys.stdin.readline

#정사각형 4개를 이어 붙인 폴리오미노는 테트로미노
N, M  = map(int, input().split())

paper = [list(map(int, input().split())) for _ in range(M)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(x, y):
    if 0<=x<N and 0<= y < M:
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if 0<= next_x < N and 0<=next_y<M:
                paper[next_x][next_y]
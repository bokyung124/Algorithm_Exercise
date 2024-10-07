import copy
import sys

# 8방향 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 물고기 이동 함수
def move_fish(space, sx, sy):
    for i in range(1, 17):
        x, y = -1, -1
        for j in range(4):
            for k in range(4):
                if space[j][k][0] == i:
                    x, y = j, k
                    break
            if x != -1:
                break
        
        if x == -1:  # 물고기가 없는 경우
            continue
        
        direction = space[x][y][1]
        
        for _ in range(8):
            nx, ny = x + dx[direction], y + dy[direction]
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (sx, sy):
                space[x][y][1] = direction
                space[x][y], space[nx][ny] = space[nx][ny], space[x][y]
                break
            direction = (direction + 1) % 8

# 상어 이동 가능한 위치 찾기
def get_possible_positions(space, sx, sy):
    direction = space[sx][sy][1]
    positions = []
    for i in range(1, 4):
        nx, ny = sx + dx[direction] * i, sy + dy[direction] * i
        if 0 <= nx < 4 and 0 <= ny < 4 and space[nx][ny][0] > 0:
            positions.append((nx, ny))
    return positions

# DFS로 최대 점수 찾기
def dfs(space, sx, sy, total):
    global max_score
    
    # 현재 위치의 물고기 먹기
    score = space[sx][sy][0]
    space[sx][sy][0] = -1  # 상어 표시
    
    # 물고기 이동
    move_fish(space, sx, sy)
    
    # 상어 이동 가능한 위치 찾기
    positions = get_possible_positions(space, sx, sy)
    
    # 이동할 수 있는 위치가 없으면 종료
    if not positions:
        max_score = max(max_score, total + score)
        return
    
    # 가능한 모든 위치로 이동
    for nx, ny in positions:
        new_space = copy.deepcopy(space)
        dfs(new_space, nx, ny, total + score)

# 메인 함수
def solve():
    space = [[[0, 0] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(4):
            space[i][j] = [row[j*2], row[j*2+1]-1]
    
    global max_score
    max_score = 0
    dfs(space, 0, 0, 0)
    sys.stdout.write(str(max_score)) 

solve()
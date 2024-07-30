from collections import deque
from sys import stdin, stdout

def solution(N, K, apples, L, directions):
    board = [[0] * (N+1) for _ in range(N+1)]

    apple_set = set(map(tuple, apples))

    dir_changes = dict(directions)
  
    snake = deque([(1, 1)])
    direction = 0  

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    time = 0
    
    while True:
        time += 1

        nx = snake[0][0] + dx[direction]
        ny = snake[0][1] + dy[direction]
        
        if nx < 1 or nx > N or ny < 1 or ny > N or (nx, ny) in snake:
            return time

        snake.appendleft((nx, ny))

        if (nx, ny) in apple_set:
            apple_set.remove((nx, ny))
        else:
            snake.pop()

        if time in dir_changes:
            if dir_changes[time] == 'L':
                direction = (direction - 1) % 4
            else:
                direction = (direction + 1) % 4

N = int(stdin.readline())
K = int(stdin.readline())
apples = [tuple(map(int, stdin.readline().split())) for _ in range(K)]
L = int(stdin.readline())
directions = {int(x): c for x, c in (stdin.readline().split() for _ in range(L))}

result = solution(N, K, apples, L, directions)
stdout.write(str(result))
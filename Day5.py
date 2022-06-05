from sys import stdin
from collections import deque


n, m = map(int, stdin.readline().split())

# 지도를 나타내는 2차원 배열
new_maze = []

for _ in range(n):
    # rstrip() 함수로 줄바꿈 문자('\n')를 처리
    new_maze.append([int(x) for x in stdin.readline().rstrip()])

# 최단 거리를 저장하는 2차원 배열
shortest = [[0] * m for _ in range(n)]
# 초기값 설정 : (0, 0)은 자기 자신만을 지나야 하므로 1
shortest[0][0] = 1


# BFS 알고리즘으로 미로 찾기
def get_distance(maze, end_r, end_c, dist):
    queue = deque()
    queue.append((0, 0))

    dist[0][0] = 1

    # 더 이상 탐색할 칸이 없을 때까지 너비 우선 탐색
    while queue:
        r, c = queue.popleft()

        # 맨 아래쪽 줄이 아니라면
        if r < end_r:
            if maze[r + 1][c] == 1 and dist[r + 1][c] == 0:
                dist[r + 1][c] = dist[r][c] + 1
                queue.append((r + 1, c))

        # 맨 오른쪽 줄이 아니라면
        if c < end_c:
            if maze[r][c + 1] == 1 and dist[r][c + 1] == 0:
                dist[r][c + 1] = dist[r][c] + 1
                queue.append((r, c + 1))

        # 맨 위쪽 줄이 아니라면
        if r > 0:
            if maze[r - 1][c] == 1 and dist[r - 1][c] == 0:
                dist[r - 1][c] = dist[r][c] + 1
                queue.append((r - 1, c))

        # 맨 왼쪽 줄이 아니라면
        if c > 0:
            if maze[r][c - 1] == 1 and dist[r][c - 1] == 0:
                dist[r][c - 1] = dist[r][c] + 1
                queue.append((r, c - 1))

    return dist[end_r][end_c]


distance = get_distance(new_maze, n - 1, m - 1, shortest)
print(distance)

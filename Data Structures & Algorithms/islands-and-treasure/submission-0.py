from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        # 모든 보물 상자를 한번에 q에 넣고 BFS 단 한번 수행
        m,n = len(grid), len(grid[0])
        
        n_x = [1,0,-1,0]
        n_y = [0,-1,0,1]

        q = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            c_x, c_y = q.popleft()

            for i in range(4):
                next_x, next_y = c_x + n_x[i], c_y + n_y[i]

                if (
                    next_x < 0 or next_x >= m or
                    next_y < 0 or next_y >= n
                ):
                    continue
                
                if grid[next_x][next_y] == INF:
                    q.append((next_x,next_y))
                    grid[next_x][next_y] = grid[c_x][c_y] + 1
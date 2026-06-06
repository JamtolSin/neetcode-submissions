from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 가로,세로 (1~10)
        row, col = len(grid), len(grid[0])
        
        # 방문 기록
        visited = [[-1] * col for _ in range(row)]

        # 다음 방문 위치 [동,서,남,북]
        r_move = [1,0,-1,0]
        c_move = [0,-1,0,1]

        q = deque()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    visited[r][c] = 0
                    q.append((r,c))
        
        while q:
            cu_r, cu_c = q.popleft()
            
            for i in range(4):
                ne_r, ne_c = cu_r + r_move[i], cu_c + c_move[i]

                if (
                    ne_r < 0 or ne_c < 0 or
                    ne_r >= row or ne_c >= col
                ):
                    continue

                if visited[ne_r][ne_c] != -1:
                    continue
                
                if grid[ne_r][ne_c] == 1:
                    visited[ne_r][ne_c] = visited[cu_r][cu_c] + 1
                    q.append((ne_r,ne_c))

        max_time = 0

        for r in range(row):
            for c in range(col):
                if visited[r][c] == -1 and grid[r][c] != 0:
                    return -1
                else:
                    max_time = max(visited[r][c], max_time)
        
        return max_time
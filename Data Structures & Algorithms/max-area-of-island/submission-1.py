class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_island = 0 # island 개수
        rows = len(grid)
        cols = len(grid[0])

        # 방문했는지 체크리스트
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def BFS(row, col):
            # 상하좌우
            row_move = [1,0,-1,0]
            col_move = [0,-1,0,1]

            q = deque()
            q.append((row,col))
            visited[row][col] = 1
            cu_island = 1 # 현재 땅

            while q:
                cu_r, cu_c = q.popleft()

                for i in range(4):
                    next_row = cu_r + row_move[i]
                    next_col = cu_c + col_move[i]

                    if (
                        0 <= next_row < rows and
                        0 <= next_col < cols and
                        visited[next_row][next_col] == 0 and
                        grid[next_row][next_col] == 1
                    ):
                        visited[next_row][next_col] = 1
                        cu_island += 1 # 현재 땅 개수 추가
                        q.append((next_row,next_col))
            
            return cu_island # 현재 땅 개수 반환

        # 1. 해당 칸 방문했는지 체크 - 안했으면 BFS 실행
        for row in range(rows):
            for col in range(cols):
                if visited[row][col] == 0 and grid[row][col] == 1:
                    cu_i = BFS(row,col)
                    max_island = max(max_island, cu_i) # 가장 큰 땅 개수 갱

        
        return max_island
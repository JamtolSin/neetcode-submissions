class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        from collections import deque

        row, col = len(heights), len(heights[0])
        
        # Pacific으로 흘러갈 수 있는 칸
        P_visited = [["F"]*col for _ in range(row)]
        # Atlantic으로 흘러갈 수 있는 칸
        A_visited = [["F"]*col for _ in range(row)]

        # Pacific BFS
        P_q = deque()

        for i in range(row):
            P_q.append((i,0))
            P_visited[i][0] = "T"
        for j in range(1,col):
            P_q.append((0,j))
            P_visited[0][j] = "T"
        
        # Atlantic BFS
        A_q = deque()

        for i in range(row):
            A_q.append((i,col-1))
            A_visited[i][col-1] = "T"
        for j in range(0,col-1):
            A_q.append((row-1,j))
            A_visited[row-1][j] = "T"

        r_move = [1,0,-1,0]
        c_move = [0,-1,0,1]

        while P_q:
            cu_r, cu_c = P_q.popleft()

            for i in range(4):
                ne_r, ne_c = cu_r + r_move[i], cu_c + c_move[i]

                # 범위 밖
                if ne_r < 0 or ne_r >= row or ne_c < 0 or ne_c >= col:
                    continue
                
                # 높이 조건
                if heights[cu_r][cu_c] > heights[ne_r][ne_c]:
                    continue

                # 방문 여부
                if P_visited[ne_r][ne_c] == "F":
                    P_visited[ne_r][ne_c] = "T"
                    P_q.append((ne_r,ne_c))

        while A_q:
            cu_r, cu_c = A_q.popleft()

            for i in range(4):
                ne_r, ne_c = cu_r + r_move[i], cu_c + c_move[i]

                # 범위 밖
                if ne_r < 0 or ne_r >= row or ne_c < 0 or ne_c >= col:
                    continue
                
                # 높이 조건
                if heights[cu_r][cu_c] > heights[ne_r][ne_c]:
                    continue

                # 방문 여부
                if A_visited[ne_r][ne_c] == "F":
                    A_visited[ne_r][ne_c] = "T"
                    A_q.append((ne_r,ne_c))

        answer = []
        for i in range(row):
            for j in range(col):
                if P_visited[i][j] == "T" and A_visited[i][j] == "T":
                    answer.append([i,j])
        
        return answer
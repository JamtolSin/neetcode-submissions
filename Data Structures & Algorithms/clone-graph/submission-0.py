"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        # 빈 그래프
        if not node:
            return None

        # 복사 노드
        old_to_new = {}

        # 시작 노드 복사
        old_to_new[node] = Node(node.val)

        q = deque([node])

        while q:
            cur_node = q.popleft()

            # 현재 노드의 이웃 탐색
            for neighbor in cur_node.neighbors:
                
                # 아직 복사 안한 노드면 생성
                if neighbor not in old_to_new:
                    old_to_new[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                
                # 복사된 현대 노드에 이웃 연결
                old_to_new[cur_node].neighbors.append(
                    old_to_new[neighbor]
                )
        
        return old_to_new[node]
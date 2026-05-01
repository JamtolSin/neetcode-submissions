# time - O(n) / space - O(n)

# 1. 전체 리스트를 돌며 가장 큰 수 big_1, big_2 탐색

# 2. 양쪽 big_1, big_2 사이의 수들을 min(big_1, big_2)값을 빼 숫자 더하기

# 3. big_1기준으로 왼쪽, big_2기준으로 오른쪽으로 진행하면서 다음 큰 값 찾기

# 4. 2&3과정 반복

# 5. 더한 값 return

# class Solution:
#     def trap(self, height: List[int]) -> int:
        
#         big_1, big_2 = int(0), int(len(height))
#         water_height = int(0)

# 다시 해당 방법은 O(n^2) 걸리지 않을까 싶음 - 처음 n개를 서치 -> 반복 / 최악의 경우 n^2

"""
차라리 처음 부터 계산 하는 방식으로 n 시간 사용 방식

그럼 처음부터 해당 좌표 i에서 좌측 기준으로 max값, 우측 기준으로 max값을 저장하는 list 만드는것은?
"""

class Solution:
    """
    1. water - 물 높이[return 값], l_max & r_max - 해당 좌표 기준 좌측으로 max 값 & 우측으로 max 값
    """
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        water = 0

        l_max = [0] * n
        r_max = [0] * n

        l_max[0] = height[0]
        r_max[n-1] = height[n-1]

        for i in range(1,n):
            l_max[i] = max(l_max[i-1], height[i])
        
        for j in range(n-2, -1, -1):
            r_max[j] = max(r_max[j+1], height[j])
        
        for k in range(n):
            water += min(l_max[k], r_max[k]) - height[k]
        
        return water
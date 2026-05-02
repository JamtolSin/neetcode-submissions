class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        O(log(m*n)) 시간
        1. 각 row의 첫번째 수 중 가운데 위치의 row 서치 [n//2]
        [서치] <- 2번 반복
        2. 다음 row 수 비교 [if matrix[i][j] <= target] 다음 row가 target보다 작은 경우 진행
        2-1. 만약 더 작은 경우 target_row 한칸 씩 축소
        3. 해당 row 전수 비교
        """

        # n = len(matrix)
        # target_row = n//2

        # while True:
        #     if matrix[target_row][0] <= target:
        #         if matrix[target_row][-1] >= target:
        #             for check in matrix[target_row]:
        #                 if check == target:
        #                     return True
        #             return False
        #         else:
        #             target_row += 1
        #     else:
        #         if matrix[target_row - 1][-1] <= target:
        #             return False
        #         else:
        #             if target_row != 0:
        #                 target_row -= 1
        #             else:
        #                 return False

        # 이렇게 구현하면 계속적으로 예외 케이스에 조건을 추가해야해 에러 발생 가능이 높음
        # 2차원 배열을 1차원 배열로 수정하여 다시 진행 해보자

        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:

            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
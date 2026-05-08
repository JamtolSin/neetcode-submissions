def find_k(piles: List[int], k: int) -> int:
    """
    piles - 바나나 뭉치
    k - 한번에 먹을 바나나
    h (hours) 리턴하는 함수
    """
    answer = 0

    for i in piles:
        answer += (i + k -1) // k
    
    return answer

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        answer = end

        while start <= end:
            mid = (start + end) // 2
            
            k = find_k(piles, mid) 

            if k <= h:
                answer = mid
                end = mid - 1
            elif k > h:
                start = mid + 1
        
        return answer
            

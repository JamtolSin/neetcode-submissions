class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for p1 in range(len(numbers)-1):
            for p2 in range(p1+1,len(numbers)):
                if numbers[p1] + numbers[p2] == target:
                    return [p1+1, p2+1]
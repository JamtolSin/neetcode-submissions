# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         ans = set()
#         nums.sort()
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         tmp = [nums[i], nums[j], nums[k]]
#                         ans.add(tuple(tmp))
        
#         return [list(i) for i in ans]

# set은 내부적으로 hash 기반 구조라서 변하지 않는 값만 저장 가능 -> list는 변하기 때문에 금지

# 위 코드는 TLE (Time Limit Exceeded) 발생
# n ^ 3 방식을 n ^ 2으로 변경 필요



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1 # sort 된 상태라 숫자는 오름차순

                else:
                    right -= 1
        
        return [list(t) for t in ans]
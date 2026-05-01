# 앞과 뒤가 같은 문자 true
# two pointer 활용 문제

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         filtered = []

#         for c in s:
#             if c.isalnum():
#                 filtered.append(c.lower())

#         left, right = 0, len(filtered) - 1

#         while left < right:
#             if filtered[left] != filtered[right]:
#                 return False
#             else:
#                 left += 1
#                 right -= 1
        
#         return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]

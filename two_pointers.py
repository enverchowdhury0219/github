# two pointers

# day 8

# valid palindrome

# solution

# A palindrome string is a string that is read the same from the start as well as from the end. This means the character at the start should match the character at the end at the same index. We can use the two pointer algorithm to do this efficiently.

# O(n) time and O(1) space, where n is the length of the input string (for the two pointer solution)

# reverse string way:
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         newStr = '' # making this new string takes up memory
#         for c in s:
#             if c.isalnum(): # built in alpha numeric function
#                 newStr += c.lower()
#         return newStr == newStr[::-1] # [::-1] is how we reverse a string
# 
# two pointers way:
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1

#         while l < r:
#             while l < r and not self.alphaNum(s[l]):  # to call another function inside an object, we have to use self keyword
#                 l += 1
#             while r > l and not self.alphaNum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():    (here x is .)
#                 return False
#             l, r = l + 1, r - 1
#         return True

#     def alphaNum(self, c):
#         return (ord('A') <= ord(c) <= ord('Z') or        # using ascii value to compare to the character to characters that are alpha numeric
#                 ord('a') <= ord(c) <= ord('z') or
#                 ord('0') <= ord(c) <= ord('9'))

# day 9

# 3sum

# solution: 
# To efficiently find the j and k pairs, we run the two pointer approach on the elements to the right of index i as the array is sorted. When we run two pointer algorithm, consider j and k as pointers (j is at left, k is at right) and target = -nums[i], if the current sum num[j] + nums[k] < target then we need to increase the value of current sum by incrementing j pointer. Else if the current sum num[j] + nums[k] > target then we should decrease the value of current sum by decrementing k pointer. How do you deal with duplicates?

# When the current sum nums[j] + nums[k] == target add this pair to the result. We can move j or k pointer until j < k and the pairs are repeated. This ensures that no duplicate pairs are added to the result.

# time and space complexity - O(nlogn) for sorting + O(n^2) for the two loops which then becomes O(n^2) and space could be either O(1) or O(n) if sorting takes space in your library

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()

#         for i, a in enumerate(nums): # When iterating through a sequence, enumerate() yields pairs of (index, value) tuples
#             if a > 0:
#                 break

#             if i > 0 and a == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1
#             while l < r:
#                 threeSum = a + nums[l] + nums[r]
#                 if threeSum > 0:
#                     r -= 1
#                 elif threeSum < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1

#         return res

# day 10

# container with most water

# solutiuon:

# We can use the two pointer algorithm. One pointer is at the start and the other at the end. At each step, we 
# calculate the amount of water using the formula (j - i) * min(heights[i], heights[j]). Then, we move the pointer 
# that has the smaller height value. Can you think why we only move the pointer at smaller height?

# In the formula, the amount of water depends only on the minimum height. Therefore, it is appropriate to replace 
# the smaller height value.

# time - O(n), space - O(1)

# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         l, r = 0, len(heights) - 1
#         res = 0

#         while l < r:
#             area = min(heights[l], heights[r]) * (r - l)
#             res = max(res, area)
#             if heights[l] <= heights[r]:
#                 l += 1
#             else:
#                 r -= 1
#         return res


# brute force:

# class Solution:
#     def maxArea(self, heights: List[int]) -> int:
#         res = 0
#         for i in range(len(heights)):
#             for j in range(i + 1, len(heights)):
#                 res = max(res, min(heights[i], heights[j]) * (j - i))
#         return res





# stack

# day 14

# valid parentheses

# solution:  O(n) time and O(n) space, where n is the length of the given string.

# how far i got: 
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         for i in range(len(s)):
#             if s[i] == '[' or  s[i] == '{' or s[i] == '(':
#                 stack.append(s[i])

# solution:
# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

#         for c in s:  # this will go over the each character
#             if c in closeToOpen: # this will check if the caharacter is a closed bracket
#                 if stack and stack[-1] == closeToOpen[c]: # this checks if the top of the stack has a corresponding opening bracket
#                     stack.pop()  # removing the element from the stack
#                 else:
#                     return False
#             else:
#                 stack.append(c)

#         return True if not stack else False


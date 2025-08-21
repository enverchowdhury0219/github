# sliding window

# day 10 

# best time to buy and sell stock

# my solution (ran with test cases given, but not all):  class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profit = 0
#         l,r = 0, len(prices) - 1
#         while l < r:
#             profit = max(profit, prices[r] - prices[l])
#             if prices[r] < prices[l]:
#                 r -= 1
#             l += 1
#         return profit

# solution (two pointer approach):

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l, r = 0, 1
#         maxP = 0

#         while r < len(prices):
#             if prices[l] < prices[r]:
#                 profit = prices[r] - prices[l]
#                 maxP = max(maxP, profit)
#             else:
#                 l = r # we want our left pointer to be the lowest, so if prices[r] is lower, we would want to be there
#             r += 1
#         return maxP

# day 11

# longest substring without repeating characters

# my solution (too inefficent so it did not run):  class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         count_so_far = 0
#         maxCount = 0
#         l, r = 0, len(s) - 1
#         while l < r:
#             if chr(l) < chr(l+1):
#                 count_so_far += 1
#             else:
#                 count_so_far = 0
#                 l += 1
#         maxCount = max(maxCount, count_so_far)
#         return maxCount
 

# solution:

# We can iterate through the given string with index r as the right boundary and l as the left boundary of the window. 
# We use a hash set to check if the character is present in the window or not. When we encounter a character at index r 
# that is already present in the window, we shrink the window by incrementing the l pointer until the window no longer 
# contains any duplicates. Also, we remove characters from the hash set that are excluded from the window as the l 
# pointer moves. At each iteration, we update the result with the length of the current window, r - l + 1, if this length 
# is greater than the current result.

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         charSet = set()
#         l = 0
#         res = 0

#         for r in range(len(s)):
#             while s[r] in charSet:    # we make sure that our set does not have any duplicates, so we increase l to shorten our window
#                 charSet.remove(s[l])
#                 l += 1
#             charSet.add(s[r]).   # when we reach a non duplicate caharcter - the start of our set would be set to the caharcter at index r
#             res = max(res, r - l + 1). # r - l + 1 would measure the size of our window and hence the longest substring
#         return res

# day 12

# longest repeating character replacement (this is tough)

# solution:We can use the sliding window approach. The window size will be dynamic, and we will shrink the window 
# when the number of replacements exceeds k. The result will be the maximum window size observed at each iteration.

# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         res = 0
#         charSet = set(s)

#         for c in charSet:
#             count = l = 0
#             for r in range(len(s)):
#                 if s[r] == c:
#                     count += 1

#                 while (r - l + 1) - count > k:
#                     if s[l] == c:
#                         count -= 1
#                     l += 1

#                 res = max(res, r - l + 1)
#         return res

# ai explanation:This code finds the length of the longest substring in s that can be made of the same 
# character by replacing at most k other characters. It first gets all unique characters in s and then tests each one 
# as the “target” character. For a given target character c, it uses a sliding window (l for left, r for right) to keep 
# track of how many characters inside the window match c (count). If the number of characters that don’t match c in the 
# window exceeds k, it moves the left pointer l forward to shrink the window until it’s valid again. When it moves l, if 
# the character at l is c, it decrements count because that matching character is no longer inside the window. This ensures 
# count always reflects only the matches currently in the window. Throughout the process, it keeps track of the largest valid 
# window length found across all target characters and returns it.

# day 13

# minimum window substring (hard)

# solution:

# * Time complexity: O(n)
# * Space complexity: O(m)
# Where n is the length of the string s and m is the total number of unique characters in the strings t and s. 
#   class Solution:
#     def minWindow(self, s: str, t: str) -> str:
#         if t == "":
#             return ""

#         countT, window = {}, {}
#         for c in t:
#             countT[c] = 1 + countT.get(c, 0)

#         have, need = 0, len(countT)
#         res, resLen = [-1, -1], float("infinity")
#         l = 0
#         for r in range(len(s)):
#             c = s[r]
#             window[c] = 1 + window.get(c, 0)

#             if c in countT and window[c] == countT[c]:
#                 have += 1

#             while have == need:
#                 if (r - l + 1) < resLen:
#                     res = [l, r]
#                     resLen = r - l + 1

#                 window[s[l]] -= 1
#                 if s[l] in countT and window[s[l]] < countT[s[l]]:
#                     have -= 1
#                 l += 1
#         l, r = res
#         return s[l : r + 1] if resLen != float("infinity") else ""

# ai explanantion: This is a sliding window algorithm for finding the smallest substring in s that contains 
# all the characters in t.

# Step-by-step breakdown
# 1️⃣ Special case — empty t
# if t == "":
#     return ""
# If t is empty, there’s no substring to find, so return an empty string.

# 2️⃣ Count characters in t
# countT, window = {}, {}
# for c in t:
#     countT[c] = 1 + countT.get(c, 0)
# * countT is a dictionary that tells you how many of each character you need from t.
# * Example: t = "ABA" → countT = {'A': 2, 'B': 1}
# * window will store counts of characters currently in your sliding window over s.

# 3️⃣ Tracking what we have vs. what we need
# have, need = 0, len(countT)
# * need = number of unique characters in t (from countT).
# * have = number of characters we’ve currently matched the needed amount for.

# 4️⃣ The result variables
# res, resLen = [-1, -1], float("infinity")
# * res will store [start_index, end_index] of the best (smallest) window.
# * resLen keeps track of that window’s length.

# 5️⃣ Expand the window (right pointer r)
# l = 0
# for r in range(len(s)):
#     c = s[r]
#     window[c] = 1 + window.get(c, 0)
# * We move the right pointer r forward through s.
# * We add the character at s[r] into our window dictionary.

# 6️⃣ Check if we matched a needed character
# if c in countT and window[c] == countT[c]:
#     have += 1
# If this character is in t and we now have the exact number needed, have goes up.

# 7️⃣ Try shrinking the window (left pointer l)
# while have == need:
#     if (r - l + 1) < resLen:
#         res = [l, r]
#         resLen = r - l + 1
# * If have == need, it means this window has all characters from t.
# * We check if it’s the smallest so far and update res.

# 8️⃣ Move l to shrink the window
# window[s[l]] -= 1
# if s[l] in countT and window[s[l]] < countT[s[l]]:
#     have -= 1
# l += 1
# * We shrink from the left to see if we can still have all needed characters but with a smaller window.
# * If removing s[l] means we no longer meet the requirement for that char, have goes down.

# 9️⃣ Return the smallest window
# l, r = res
# return s[l : r + 1] if resLen != float("infinity") else ""
# * If we found a valid window, return it.
# * If resLen was never updated, return "".

# In plain words:
# * Goal: Find the smallest chunk of s that contains every letter of t (with the right counts).
# * How it works:
#     1. Count what’s needed from t.
#     2. Use two pointers (l and r) to form a sliding window over s.
#     3. Expand r until we have all the needed characters.
#     4. Shrink l to make the window as small as possible while still valid.
#     5. Keep track of the smallest valid window found.
# * Efficiency: Runs in O(n) time because each character is visited at most twice (once when expanding, once when shrinking).
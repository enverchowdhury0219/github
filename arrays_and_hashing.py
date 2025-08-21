# arrays and hashing

# day 1 

# contains duplicate

# my solution(correct): 
# def hasDuplicate(self, nums: List[int]) -> bool:
#         for i in range (len(nums)):
#             for j in range(i+1,len(nums)):
#                 if nums[i] == nums[j]:
#                     return True
#         return False

# time complexity is O(n^2)
# space complexity is O(1) (as no extra memory is needed)

# but its brute force, as we are checking every element, we want O(n) for time complexity

# time and space complexity has a tradeoff

# we use a hashset which allows for instant comparison, so we only go through array once, but we create a hashset of space n, so the most optimal solution is O(n) time and space complexity

#     def hasDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()
#         for num in nums:
#             if num in hashset:
#                 return True
#             hashset.add(num)
#         return False

# day 2

# valid anagram (same letters of a word but diff order)

# my solutuion (correct for test cases, but not all):def isAnagram(self, s: str, t: str) -> bool:
#         for i in range(len(s)):
#             if s[i] not in t:
#                 return False
#         return True

# we simply sort the list and compare them to see if they are equal. sorted returns a list of the characters in sorted order by comparing the numerical value of the corresponding characters

# solution:
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
            
#         return sorted(s) == sorted(t)


# two sum
# my solution (correct for test cases, but not all):
# def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             num1 = nums[i]
#             num2 = target - nums[i]
#             if num2 in nums and nums.index(num1) != nums.index(num2):
#                 return sorted([i,nums.index(num2)])

# solution:

# we use a hashmap, which takes memory, but the whole array is only gone through once, so O(n) time and space complexity

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {}  # val -> index

#         for i, n in enumerate(nums):      # what this does is keep a track of the index and the object in the list, so i is the index of n in nums
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i 

# day 3

# group anagrams

# couldnt figure out this solution

# solution:
# time complexity of O(m*n), m is no of strings and n is len of lomgest string
# space complexity O(m) extra space and O(m*n) for the output list

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list) # Unlike a standard dict, which raises a KeyError when you try to access a key that doesn't exist, defaultdict automatically creates a default value for that key if it's not found.
#         for s in strs:
#             count = [0] * 26
#             for c in s:
#                 count[ord(c) - ord('a')] += 1 # using ascii value
#             res[tuple(count)].append(s) # we change it to a tuple here as in python, lists cannot be keys as they are mutable
#         return list(res.values())

# # ai explanation:

# # Code Breakdown:
# # 1. res = defaultdict(list):
# #     * This line initializes a defaultdict named res.
# #     * The key aspect here is list as the default factory. As explained by LabEx, when you try to access a key in res that doesn't exist, it will automatically create a new empty list ([]) as the value for that key instead of raising a KeyError. This simplifies the grouping process considerably.
# # 2. for s in strs::
# #     * The code iterates through each string s in the input list strs.
# # 3. count = [0] * 26:
# #     * For each string s, a list called count is initialized.
# #     * It contains 26 zeros, one for each lowercase English letter (a-z).
# #     * This list will be used to store the frequency of each character in the current string s.
# # 4. for c in s::
# #     * This nested loop iterates through each character c within the current string s.
# # 5. count[ord(c) - ord('a')] += 1:
# #     * This is where the character frequency counting happens.
# #     * ord(c) returns the ASCII (numerical) value of the character c. For example, ord('a') is 97, ord('b') is 98, and so on.
# #     * ord(c) - ord('a') calculates the offset of the character c from 'a'. For example, if c is 'b', ord('b') - ord('a') will be 1, so count[1] will be incremented.
# #     * This way, count[0] stores the frequency of 'a', count[1] stores the frequency of 'b', and so on.
# # 6. res[tuple(count)].append(s):
# #     * This is the crucial step for grouping.
# #     * tuple(count): The count list (which stores character frequencies) is converted into a tuple. As stated by Stack Overflow, lists are mutable and thus cannot be used directly as dictionary keys in Python. Tuples, however, are immutable and hashable, making them suitable for use as keys.
# #     * res[tuple(count)]: This uses the character frequency tuple as the key in the res defaultdict. If this key doesn't exist, defaultdict automatically creates a new empty list as its value.
# #     * .append(s): The original string s is then appended to the list associated with that specific character frequency tuple. All anagrams will have the same character frequency tuple and therefore will be grouped together in the same list.
# # 7. return list(res.values()):
# #     * Finally, the code returns a list containing all the values from the res defaultdict. Each value is a list of strings that are anagrams of each other. 

# # day 4

# # top k frequent elements

# my solution(solved one of the test cases):class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         result = []
#         for num in nums:
#             if num not in count:
#                 count[num] = 1
#             else:
#                 count[num] += 1
#                 if count[num] == k:
#                     result.append(num)
#         return result

# solution: Use the bucket sort algorithm to create n buckets, grouping numbers based on their frequencies 
# from 1 to n. Then, pick the top k numbers from the buckets, starting from n down to 1.


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         freq = [[] for i in range(len(nums) + 1)]

#         for num in nums:
#             count[num] = 1 + count.get(num, 0) # it will return 0 (default value) if it doesnta;ready exist in the hash map
#         for num, cnt in count.items(): # count.items() will return every key value pair
#             freq[cnt].append(num)

#         res = []
#         for i in range(len(freq) - 1, 0, -1): # going from the front of the list to the back
#             for num in freq[i]:
#                 res.append(num)
#                 if len(res) == k:
#                     return res

# time and space complexity of O(n)


# day 5

# encode and decode strings

# couldnt figure this out 

# my approach for the encode:
# def encode(self, strs: List[str]) -> str:
#         res = ''
#         for string in strs:
#             res.join(str)
#         return res


# solution: We can use an encoding approach where we start with a number representing the length of the string, 
# followed by a separator character (let's use # for simplicity), and then the string itself. 
# To decode, we read the number until we reach a #, then use that number to read the specified number of 
# characters as the string.

#  # example: [“abbu”, “ammu”] would encode to ‘4#abbu4#ammu’, where the integer is the length of that string

# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         res = ''
#         for s in strs:
#             res += str(len(s)) + '#' + s 
#         return res

#     def decode(self, s: str) -> List[str]:
#         res, i = [], 0

#         while i < len(s):
#             j = i
#             while s[j] != '#': 
#                 j += 1
#             length = int(s[i:j])
#             res.append(s[j+1:j+1+length])
#             i = j + 1 + length
#         return res

# time complexity: O(m) for each encode () and decode() functuon calls, m is the length of all the strings 
# and n is the number of strings
# spcace complexity: O(m + n) for each encode() and decode() function calls

# day 6

# products of array except self

# couldnt solve this

# solution:We can use the stored prefix and suffix products to compute the result array by iterating through the array 
# and simply multiplying the prefix and suffix products at each index.

# time and space complexity: O(n) (O(1) space complexity if the extra array doesnt count for extra space). 
# here x= is *=

# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         res = [1] * (len(nums))

#         prefix = 1
#         for i in range(len(nums)):
#             res[i] = prefix
#             prefix  *= nums[i]
#         postfix = 1
#         for i in range(len(nums) - 1, -1, -1): # going backwards in the array
#             res[i] *= postfix
#             postfix *= nums[i]
#         return res

# day 7

# longest consecutive sequence

# couldnt solve it

# solution:
# We can consider a number num as the start of a sequence if and only if num - 1 does not exist in the given array. 
# We iterate through the array and only start building the sequence if it is the start of a sequence. 
# This avoids repeated work. We can use a hash set for O(1) lookups by converting the array to a hash set.

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         numSet = set(nums) # using a hash set
#         longest = 0

#         for num in numSet:
#             if (num - 1) not in numSet:
#                 length = 1
#                 while (num + length) in numSet:
#                     length += 1
#                 longest = max(length, longest)
#         return longest
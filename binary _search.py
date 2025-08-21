# binary search

# day 15

# find minimum in rotated sorted array

# solution:

# This algorithm finds the minimum element in a rotated sorted array using binary search. It starts with two pointers (l at the left and r at the right) and keeps track of the current minimum (res). If the subarray between l and r is already sorted, the leftmost element is the minimum and we can stop. Otherwise, it checks the middle element (m). If the middle element is greater than or equal to the left element, that means the minimum must be in the right half, so it moves l forward. Otherwise, the minimum lies in the left half, so it moves r backward. By updating res along the way, the algorithm narrows down to the minimum in O(log n) time.

# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         res = nums[0]    # we chose this randomly
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             if nums[l] < nums[r]:
#                 res = min(res, nums[l])
#                 break    # break statements make the loop itself exit completely.

#             m = (l + r) // 2
#             res = min(res, nums[m])
#             if nums[m] >= nums[l]:
#                 l = m + 1
#             else:
#                 r = m - 1
#         return res

# day 16

# search in rotated sorted array

# solution:

# time - O(log N), soace - O(1)

# Let’s walk the code on nums = [4,5,6,0,1,2,3] with target = 2:
# 1. Start: l=0, r=6. mid=(0+6)//2=3 → nums[mid]=0. Not the target.
# * Check which half is sorted: nums[l]=4 <= nums[mid]=0 is false, so the right half (mid..r) is sorted: [0,1,2,3].
# * Does the target lie in that sorted half? The code checks: target < nums[mid] (2<0) or target > nums[r] (2>3) → both false, so target is inside. Move left pointer right: l = mid + 1 = 4.
# 1. Now l=4, r=6.mid=(4+6)//2=5 → nums[mid]=2 which equals the target → return 5.
# Why this works: at each step, the code identifies the sorted half (nums[l] <= nums[mid] means left is sorted; otherwise 
# right is sorted) and then checks if the target falls within that half’s bounds. If yes, it narrows to that half; if not, it 
# searches the other half. Here it takes just two iterations to find index 5.

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             mid = (l + r) // 2
#             if target == nums[mid]:
#                 return mid

#             # left side of the array
#             if nums[l] <= nums[mid]:
#                 if target > nums[mid] or target < nums[l]:
#                     l = mid + 1
#                 else:
#                     r = mid - 1
#             # right side of the array
#             else:
#                 if target < nums[mid] or target > nums[r]:
#                     r = mid - 1
#                 else:
#                     l = mid + 1
#         return -1


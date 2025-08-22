# linked list

# day 17

# reverse linked list

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         prev, curr = None, head

#         while curr:
#             temp = curr.next   # this is curr.next
#             curr.next = prev   # this is curr.next
#             prev = curr
#             curr = temp
#         return prev

# day 18

# merge two sorted linked lists

# my solution(some syntax errors with linked list):

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         curr1 = list1
#         curr2 = list2
#         res = ListNode()
#         while curr1 and curr2:
#             if curr1.val <= curr2.val:
#                 res.next(curr1.val)
#             else:
#                 res.next(curr2.val)
#             curr1 = curr1.next
#             curr2 = curr2.next
#         return res

# solution:

# Time complexity: O(n + m) where n is the len of list1 and m is the len of list2
# Space: O(1)

# we use the technique of the dummy node so we dont have to worry about the edge case of inserting into an empty list  # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
#         dummy = node = ListNode()

#         while list1 and list2:
#             if list1.val < list2.val:
#                 node.next = list1
#                 list1 = list1.next
#             else:
#                 node.next = list2
#                 list2 = list2.next
#             node = node.next

#         node.next = list1 or list2

#         return dummy.next

# day 19

# linked list cycle detection

# solution:

# time and space - O(n)
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         seen = set()
#         cur = head
#         while cur:
#             if cur in seen:
#                 return True
#             seen.add(cur)
#             cur = cur.next
#         return False

# day 20

# reorder list

# The code reorders a singly linked list into the pattern `L0 → Ln → L1 → Ln-1 → L2 → Ln-2 …`. It first finds the 
# middle of the list using slow and fast pointers, where `slow` ends at the midpoint. Then it splits the list into two halves
# and reverses the second half. Finally, it merges the two halves by alternating nodes from the first half and the reversed 
# second half, weaving them together into the required reordered structure.

# time - O(n), where n is the number of nodes. space - O(1)

# reverse and merge:
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def reorderList(self, head: Optional[ListNode]) -> None:
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next

#         second = slow.next
#         prev = slow.next = None
#         while second:
#             tmp = second.next
#             second.next = prev
#             prev = second
#             second = tmp

#         first, second = head, prev
#         while second:
#             tmp1, tmp2 = first.next, second.next
#             first.next = second
#             second.next = tmp1
#             first, second = tmp1, tmp2


# day 21

# remove nth Node from end of linked list

# solution:

# time - O(N)
# space - O(1)

# two pointer approach:  # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
